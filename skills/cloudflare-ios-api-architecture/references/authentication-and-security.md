# Authentication and Security

## Identity and application sessions

An identity provider proves identity during sign-in. The API then creates an application session for normal API requests.

The app does not use an identity-provider token as its permanent API credential. This separation gives the API control over session lifetime and revocation.

For a native iOS app, Sign in with Apple is one identity option. Better Auth is one session-service option for a Cloudflare Worker.

Another identity or session service can replace these products. The replacement must preserve the rules in this document.

## Sign-in flow

1. The iOS app starts the native identity flow.
2. The iOS app creates the required nonce or proof value.
3. The identity provider returns a short-lived identity credential.
4. The iOS app sends the credential to the Worker over HTTPS.
5. The session service validates the credential and its claims.
6. The session service creates or loads the application user.
7. The session service creates an application session.
8. The iOS app stores the session token in Keychain.

The server validates the signature, issuer, audience, expiration, and replay-protection value. The server also validates all provider-required claims.

## Session storage

The iOS app stores the application session token in Keychain. It does not store the token in `UserDefaults` or SwiftData.

Use a device-only Keychain accessibility value for an interactive app. Use an after-first-unlock value only when background requests require the token.

The session service stores server session state when immediate revocation is required. A database-backed session supports logout and administrative revocation.

Session lifetime is a product security policy. The configuration must define inactivity expiration, refresh behavior, and sensitive-operation freshness.

## App launch

1. Read the session token from Keychain.
2. If the token is absent, display the sign-in interface.
3. If the token is present, request the current session from the API.
4. Display protected data only after a valid session response.
5. Delete an invalid token after the API returns an authentication error.

A temporary network failure does not prove that the session is invalid. The app can display cached data that its local policy permits.

## Authorization model

Authentication identifies the principal. Authorization controls the actions that the principal can perform on each resource.

Every protected resource belongs to an authorization scope. The server derives permitted scopes from server-owned membership or policy records.

A client-supplied scope identifier does not grant access. The Worker validates the requested action against the authenticated principal and resource.

The product can define roles later. The generic architecture requires a central authorization function with consistent decisions across all routes.

## Protected request flow

The Worker processes a protected request in this order:

1. Reject an unsupported method or content type.
2. Apply an IP rate limit to an unauthenticated route.
3. Validate the application session.
4. Load the applicable authorization policy.
5. Authorize the action on the requested resource.
6. Apply principal and scope abuse limits.
7. Validate the request body and size.
8. Run the requested service operation.
9. Record safe operational data.
10. Return or stream the response.

The API returns `401 Unauthorized` for an invalid session. It returns `403 Forbidden` for a denied action with a valid session.

## Security rules

- Store server secrets in Cloudflare secret bindings.
- Validate each identity credential on the server.
- Store application session tokens only in Keychain.
- Authenticate before authorization.
- Authorize every protected resource and context item.
- Limit request size and AI output size.
- Use a server-side model allowlist.
- Apply abuse limits to sign-in and AI routes.
- Use an authoritative control for hard spending limits.
- Do not log credentials, secrets, prompts, or private responses.
- Return generic authentication errors to clients.
- Define retention and deletion rules for user data.

## Reference implementation

The reference stack can use these products:

- [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) for native identity proof.
- [Better Auth Apple provider](https://better-auth.com/docs/authentication/apple) for Apple credential validation.
- [Better Auth bearer authentication](https://better-auth.com/docs/plugins/bearer) for native API sessions.
- [Better Auth session management](https://better-auth.com/docs/concepts/session-management) for database-backed session lifecycle.
- [Cloudflare Workers secrets](https://developers.cloudflare.com/workers/configuration/secrets/) for server secrets.

## Related documents

- [System overview](system-overview.md)
- [Application API](application-api.md)
- [Data and offline behavior](data-and-offline.md)
- [AI context](ai-context.md)
- [Operations and evolution](operations-and-evolution.md)
