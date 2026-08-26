# Application API

## Purpose and boundary

The application API serves user information and application data through versioned HTTPS endpoints. Most endpoints use resource-oriented JSON requests and responses.

The application API and AI API use the same Worker and security controls. AI output uses a different response protocol because it streams.

This document defines generic HTTP conventions. A product API specification defines the real resources, fields, filters, and operations.

## URL and format conventions

Use a major version in the public path:

```text
https://api.example.com/v1
```

The initial Cloudflare hostname can use the same path. A custom domain can replace the hostname without changing the path contract.

JSON fields use `lowerCamelCase`. Timestamps use ISO 8601 UTC strings. Resource identifiers are opaque strings.

JSON requests use these headers:

```http
Accept: application/json
Content-Type: application/json
Authorization: Bearer <session-token>
```

A request without a body does not need `Content-Type`. A public endpoint does not need `Authorization`.

## Resource endpoints

Use plural nouns for resource collections. Do not put implementation names or database table names in public paths.

| Operation | Method and path |
|---|---|
| Read the current principal | `GET /v1/me` |
| List resources | `GET /v1/resources` |
| Read one resource | `GET /v1/resources/{resourceId}` |
| Create a resource | `POST /v1/resources` |
| Change part of a resource | `PATCH /v1/resources/{resourceId}` |
| Delete a resource | `DELETE /v1/resources/{resourceId}` |

These paths are examples. Product documents replace `resources` with domain resource names.

When an operation does not fit a resource change, use an action endpoint. Sessions and AI generation are examples of distinct operations.

## Authentication and authorization

Protected endpoints require the application bearer token. The Worker validates the session before it reads or changes protected data.

The Worker authorizes every resource and operation. A path identifier or request field does not prove that the principal has access.

The API applies authorization before filtering, pagination, serialization, and cache lookup. Cached server data does not bypass authorization.

If revealing resource existence creates a security risk, the API can return `404 Not Found`. Product security policy defines this behavior.

## Reads and collections

A successful single-resource request returns the resource object directly:

```json
{
  "id": "resource-id",
  "revision": 4,
  "createdAt": "2026-08-25T12:00:00Z",
  "updatedAt": "2026-08-25T12:10:00Z"
}
```

A collection response contains items and an opaque next cursor:

```json
{
  "items": [],
  "nextCursor": "opaque-server-cursor"
}
```

The endpoint defines a stable sort order. The client does not decode or construct the cursor.

Use a bounded `limit` parameter. If the client requests a larger value, the server applies its maximum.

The product API specification defines supported filters and sort fields. The server rejects unsupported query parameters.

## Mutations and retries

The API returns the accepted server representation after a create or update. A create response uses `201 Created` and a `Location` header.

A successful update normally uses `200 OK`. A successful delete can use `204 No Content`.

Retry-sensitive mutations accept an `Idempotency-Key` header. The client reuses the key only for the same logical operation and payload.

The server scopes each key to the principal and operation. A duplicate key with a different payload returns a stable conflict error.

The iOS app can retry safe reads after temporary network failures. Mutation retries require endpoint idempotency.

When the server supplies `Retry-After`, the client obeys it. Automatic retries use a bounded delay with jitter.

## Concurrency

Writable resources expose a server revision or an entity tag. The client sends its last known value with a change request.

The server rejects a stale write instead of silently replacing newer data. The response includes enough information for the product conflict policy.

Use `409 Conflict` for application revision conflicts. When an HTTP conditional header fails, use `412 Precondition Failed`.

Use one concurrency mechanism for each resource type. Document the selected mechanism in the product API specification.

## Responses and errors

The API uses standard HTTP status codes and stable application error codes.

| Status | Meaning |
|---|---|
| `200 OK` | The read or update succeeded. |
| `201 Created` | The resource was created. |
| `204 No Content` | The operation succeeded without a response body. |
| `400 Bad Request` | The request syntax or JSON is invalid. |
| `401 Unauthorized` | The application session is missing or invalid. |
| `403 Forbidden` | The valid principal cannot perform the action. |
| `404 Not Found` | The visible resource does not exist. |
| `409 Conflict` | The resource state or idempotency state conflicts. |
| `412 Precondition Failed` | An HTTP conditional request failed. |
| `422 Unprocessable Content` | The JSON fields contain invalid values. |
| `429 Too Many Requests` | A request limit stopped the operation. |
| `5xx` | The server or a dependency failed. |

An error response uses one envelope:

```json
{
  "error": {
    "code": "resource_not_found",
    "message": "The requested resource was not found.",
    "requestId": "request-uuid",
    "details": {}
  }
}
```

The `code` value is stable and suitable for client logic. The `message` value is safe only on endpoints that permit display.

The `requestId` value connects the client error to operational records. The error does not expose secrets, SQL, stack traces, or private resource data.

## Caching and offline data

The API is authoritative. The iOS app can store permitted responses in SwiftData for fast startup and limited offline behavior.

The server can return an `ETag` for cacheable reads. The client can send `If-None-Match` and handle `304 Not Modified`.

Sensitive endpoints use `Cache-Control: no-store`. Other protected responses use a cache policy that does not permit shared public storage.

HTTP caching does not replace the synchronization cursor or mutation outbox. Each mechanism has a separate purpose.

## iOS client design

The iOS networking layer separates JSON requests from AI streams:

```text
Shared request support
├── Base URL and API version
├── Session header
├── Request identifier
└── Network policy

APIClient
├── JSON encoding and decoding
├── Application error decoding
├── Pagination
└── Idempotent retries

AIStreamClient
├── SSE parsing
├── Application AI events
├── Cancellation
└── Partial-response state
```

Domain services use `APIClient`. The AI feature uses `AIStreamClient`. Both clients use the shared request support.

Do not use SwiftData models as public API types. Map API objects to local models at the data-service boundary.

## AI API relationship

An AI generation can use `POST /v1/ai/requests`. This endpoint returns the application SSE protocol instead of a normal JSON resource.

Before the stream starts, the AI endpoint uses the same authentication, authorization, request identifiers, and JSON error envelope.

After the stream starts, the Worker reports failures with application SSE error events. Provider-specific events do not reach the iOS app.

## API specification and evolution

The architecture document defines conventions. A future `docs/api/openapi.yaml` file can define product endpoints and schemas.

OpenAPI operation identifiers and schema names become public interface names. Keep them stable across compatible product releases.

Additive fields can remain in the same major API version. A breaking path or schema change requires a new supported major version.

The server supports old app versions for the documented compatibility period. Remove an API version only after the release policy permits removal.

## Related documents

- [System overview](system-overview.md)
- [Authentication and security](authentication-and-security.md)
- [Data and offline behavior](data-and-offline.md)
- [AI API and streaming](ai-api-and-streaming.md)
- [Operations and evolution](operations-and-evolution.md)
