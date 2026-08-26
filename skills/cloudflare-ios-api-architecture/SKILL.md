---
name: cloudflare-ios-api-architecture
description: Design, review, or implement native iOS apps with Cloudflare Workers, versioned JSON APIs, D1 authoritative data, SwiftData caching, offline changes, and provider-neutral AI streaming. Use for authentication, API boundaries, persistence, AI context, model routing, or Cloudflare service decisions. Do not use for unrelated SwiftUI interface work or non-iOS Cloudflare projects.
---

# Apply the Cloudflare iOS API Architecture

Use this reference architecture as a decision tool. Keep product-specific entities, workflows, schemas, and policies in the repository.

## Start

1. Read [references/system-overview.md](references/system-overview.md) completely.
2. Find and read `docs/architecture-profile.md` when it exists.
3. Read applicable repository instructions, product documents, API specifications, configuration, and code.
4. Load only the task-specific references from the routing table.

Use this priority when guidance conflicts:

1. Current user and repository instructions.
2. The project architecture profile and accepted architecture decision records.
3. The generic references in this skill.
4. Examples and optional defaults.

Use current vendor documentation for limits, prices, beta status, configuration fields, and API signatures.

## Load task guidance

| Task | Required references |
|---|---|
| Identity, sessions, authorization, or secrets | [authentication-and-security.md](references/authentication-and-security.md) |
| Normal user or application API calls | [application-api.md](references/application-api.md) and [authentication-and-security.md](references/authentication-and-security.md) |
| SwiftData cache, offline work, synchronization, or conflicts | [data-and-offline.md](references/data-and-offline.md) and [application-api.md](references/application-api.md) |
| AI provider routing, model isolation, SSE, cancellation, or stream storage | [ai-api-and-streaming.md](references/ai-api-and-streaming.md) and [application-api.md](references/application-api.md) |
| AI context, memory, retrieval, provenance, or prompt injection | [ai-context.md](references/ai-context.md) and [authentication-and-security.md](references/authentication-and-security.md) |
| Cloudflare service selection, environments, failures, cost, or observability | [operations-and-evolution.md](references/operations-and-evolution.md) |

Read more than one reference when the task crosses boundaries. Do not load unrelated references.

## Apply the architecture

Preserve these system boundaries:

- The API owns synchronized application data.
- The iOS app uses local synchronized data as a cache.
- The Worker authenticates and authorizes protected access.
- Provider credentials and provider-specific event formats stay on the server.
- The iOS app uses application-owned JSON and SSE contracts.
- Stored content and retrieved context remain untrusted data.
- Search indexes and caches do not become authorization sources.

Adapt optional choices to the project profile. Do not add Durable Objects, Agents SDK, Vectorize, Queues, Workflows, R2, or offline mutations without a requirement.

Keep normal JSON API calls separate from AI stream decoding. Share session headers, request identifiers, network policy, and pre-stream error conventions.

Do not copy these reference documents into a repository. Record only selected options, deviations, project document links, and unresolved decisions.

Use `$cloudflare-ios-project-architecture` when the user asks to create or update that project record.

## Review existing work

Review the implementation against the project profile before generic recommendations. Report a profile violation separately from an optional improvement.

Look for boundary leaks first:

- Provider names or provider events in the iOS public contract.
- Client-controlled authorization scopes.
- Secrets outside server secret storage or iOS Keychain.
- SwiftData or D1 persistence types used as public API types.
- Retried mutations without an idempotency policy.
- Authoritative records stored only through best-effort work.
- AI context that bypasses authorization or provenance.

## Finish

Report the references that governed the work. State each project assumption, selected optional capability, and deliberate deviation.

Do not create or update a project architecture profile unless the user requests that file change.
