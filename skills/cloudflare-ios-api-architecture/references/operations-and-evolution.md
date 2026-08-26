# Operations and Evolution

## Initial services

The initial architecture uses a small Cloudflare service set.

| Service | Initial use |
|---|---|
| Workers | Public JSON and AI APIs, authorization, provider adapters, and stream conversion. |
| D1 | Sessions and relational application data. |
| Worker secrets | Identity, session, and AI provider secrets. |
| Workers Rate Limiting | Fast abuse control for selected routes. |
| AI Gateway | Provider routing, AI metrics, and AI controls. |
| Workers Observability | Logs, traces, errors, timing, and safe usage data. |

The iOS app uses `URLSession` for API requests and streams. It can use SwiftData for its local cache and outbox.

## Optional services

Add an optional service only after a requirement needs it.

| Service | Add it for |
|---|---|
| R2 | Large files and generated artifacts. |
| Queues | Asynchronous work, retries, indexing, and notifications. |
| Workflows | Durable jobs with multiple steps, retries, or long waits. |
| Durable Objects | Strongly consistent coordination and shared connection state. |
| Agents SDK | Stateful agents, tools, schedules, and resumable live connections. |
| KV | Non-critical cached values and rarely changed configuration. |
| Vectorize | Semantic search over authorized content. |
| Workers AI | Cloudflare-hosted inference and embeddings. |

D1 remains authoritative for relational application records. A search index or cache does not become an authorization source.

## Rate and cost controls

Workers Rate Limiting supplies fast abuse control. Its counters are local, permissive, and eventually consistent.

Do not use Workers Rate Limiting as exact usage accounting. Use authoritative records or provider controls for hard quotas and spending limits.

Apply limits at several levels:

- IP limits for unauthenticated routes.
- Principal limits for authenticated routes.
- Authorization-scope limits for shared capacity.
- Model and output limits for each AI request.
- Provider or AI Gateway spending limits for cost control.

The API returns a stable application error when a limit stops a request. The error does not expose private account details.

## Observability

Assign one request identifier at the public API boundary. Propagate it through the Worker, AI Gateway, provider adapter, and stored request state.

Record safe operational fields:

- Request identifier.
- Route and response status.
- Authentication and authorization outcome without credentials.
- Provider and model identifier.
- Request duration and time to first output.
- Completion, failure, or cancellation state.
- Token or usage totals when available.
- Rate-limit and spending-control outcome.

Do not record prompts or responses by default. Define a separate approval and retention policy before private content enters logs.

## Failure modes

| Failure | Required behavior |
|---|---|
| Identity provider unavailable | Preserve valid local state and report that sign-in is unavailable. |
| Session store unavailable | Reject protected server actions and keep permitted cached data read-only. |
| D1 unavailable | Stop authoritative writes and preserve unacknowledged local mutations. |
| AI Gateway unavailable | Return a stable provider-unavailable error. |
| AI provider unavailable | Apply the configured fallback or return a retryable error. |
| Stream interrupted | Keep partial output marked as incomplete. |
| Final storage fails | Mark the request unresolved and run the configured reconciliation path. |
| Spending limit reached | Stop new provider requests before generation. |

Provider fallback follows product policy. A fallback does not bypass safety, privacy, model, or cost controls.

## Environment separation

Use separate Worker deployments and D1 databases for development and production. Add a staging environment when release validation requires it.

Each environment has independent secrets, provider configuration, rate limits, and migration history. Development does not use production credentials or session records.

Use environment-specific AI Gateway configuration. This separation prevents development traffic from changing production metrics and budgets.

## Change management

Version the public API and stream protocol. Keep provider API versions inside provider adapters.

Use database migrations for D1 schema changes. Keep the iOS app compatible with the supported API versions during a staged release.

Record product-specific technology choices in architecture decision records. Include the decision, reason, alternatives, and replacement trigger.

Review vendor limits, prices, beta status, and deprecations before implementation. Link to current documentation instead of copying volatile values.

## Evolution triggers

| Requirement | Architecture change |
|---|---|
| Large files | Add R2 and authorized object endpoints. |
| Background retries | Add Queues. |
| Multi-step durable work | Add Workflows. |
| Shared live state | Add Durable Objects. |
| Resumable agent sessions | Add Agents SDK and Durable Objects. |
| Semantic retrieval | Add Vectorize while D1 remains authoritative. |
| Cloudflare-hosted inference | Add Workers AI through a provider adapter. |
| More API services | Add service bindings and a separate service boundary. |

## References

- [Cloudflare Workers](https://developers.cloudflare.com/workers/)
- [Cloudflare D1](https://developers.cloudflare.com/d1/)
- [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)
- [Workers Rate Limiting](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/)
- [Workers Observability](https://developers.cloudflare.com/workers/observability/)
- [Cloudflare service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)

## Related documents

- [System overview](system-overview.md)
- [Authentication and security](authentication-and-security.md)
- [Application API](application-api.md)
- [Data and offline behavior](data-and-offline.md)
- [AI API and streaming](ai-api-and-streaming.md)
