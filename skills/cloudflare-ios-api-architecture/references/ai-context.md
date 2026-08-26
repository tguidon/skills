# AI Context

## Purpose

AI context is authorized data that the Worker adds to an AI request. The model does not own the context store.

The Worker builds context after authentication and authorization. The iOS app does not upload its complete local database for each request.

## Context categories

Keep these categories separate:

| Category | Meaning |
|---|---|
| Source record | Current structured application data. |
| Principal context | Data that applies to one authenticated principal. |
| Scope context | Data that all authorized members of a scope can use. |
| Resource context | Data that applies to one authorized resource. |
| Conversation context | Recent messages and a summary for one conversation. |
| Retrieved segment | A relevant segment from an authorized document or record. |

Use a source record for structured application state. Do not copy the same fact into a separate context item without a clear reason.

A conversation summary compresses old messages. It does not become permanent principal or resource data.

## Authorization

Each context item has one owner scope. The Worker authorizes that scope before it reads or sends the item.

Private principal context stays private by default. A shared conversation does not receive private context without an explicit sharing rule.

Vector search does not replace authorization. Apply metadata filters before retrieval and authorize the final source record after retrieval.

## Context assembly

The Worker builds bounded context in this order:

1. Validate the application session.
2. Authorize the conversation and referenced resources.
3. Load current source records.
4. Load permitted context items.
5. Load recent conversation messages and an optional summary.
6. Remove duplicate or superseded facts.
7. Apply the context token budget.
8. Send the context and current input to the provider adapter.

Current source records take priority over summaries or stored context. Product policy resolves a conflict before permanent data changes.

## Data trust

Treat all user content, retrieved text, summaries, and context items as untrusted data. Place system rules outside these data sections.

Context cannot grant authorization. It cannot change the model allowlist, tool permissions, spending limit, or server policy.

Tool arguments require the same validation and authorization as a normal API request. Model output does not bypass server controls.

## Provenance

Each stored context item records its source, owner scope, creation time, and current status. Provenance supports user review and correction.

The product policy defines how context becomes permanent. The default policy requires explicit user intent for personal facts and preferences.

Do not infer hidden permanent context from every conversation. This behavior can preserve incorrect or unexpected personal data.

Users need controls to read, edit, and delete permanent context that refers to them. Shared context also requires an authorization policy.

## Sensitive data

Do not store credentials, session tokens, provider keys, or authentication proofs as AI context.

The product data policy identifies other prohibited data. It also defines retention, deletion, export, and provider-processing rules.

## Retrieval growth path

Use indexed D1 queries for a small, bounded context set. Add summaries when old conversation history grows beyond the request budget.

Add Vectorize when semantic retrieval is necessary. D1 remains the source of truth for authorization and final records.

Use the D1 record identifier as the vector identifier. Store authorization metadata with the vector and filter every query.

After retrieval, load the source record from D1. Then authorize it again before it enters the AI request.

## Related documents

- [System overview](system-overview.md)
- [Authentication and security](authentication-and-security.md)
- [Application API](application-api.md)
- [Data and offline behavior](data-and-offline.md)
- [AI API and streaming](ai-api-and-streaming.md)
