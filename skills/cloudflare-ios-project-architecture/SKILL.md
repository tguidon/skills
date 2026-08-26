---
name: cloudflare-ios-project-architecture
description: Create or update a small project architecture profile or focused ADR for a repository that adopts cloudflare-ios-api-architecture. Use when Codex records selected identity, API, data, offline, AI, and Cloudflare options without copying the generic architecture into the project. Do not use for ordinary implementation or broad product documentation.
---

# Create a Cloudflare iOS Project Architecture Record

Create the small project-specific layer that pairs with `$cloudflare-ios-api-architecture`.

## Load the required architecture

1. Find the installed `cloudflare-ios-api-architecture` skill.
2. Read its `SKILL.md` completely.
3. Read its `references/system-overview.md` completely.
4. Read each task-specific reference that applies to known project choices.

If the required skill is unavailable, stop. Tell the user to install `$cloudflare-ios-api-architecture` before this skill creates a project record.

The generic architecture skill is the source for available options and invariants. This skill records only project choices and deviations.

## Inspect the repository

Read these sources before drafting:

- Applicable `AGENTS.md` and `AGENTS.override.md` files.
- Existing architecture profiles and architecture decision records.
- Product requirements and domain documents.
- OpenAPI files and API documentation.
- Worker, authentication, database, and environment configuration.
- iOS persistence and networking code when it exists.
- The current Git status.

Treat implemented configuration as evidence, not as an approved decision. Preserve unrelated work and existing documentation conventions.

## Select the record type

Create `docs/architecture-profile.md` by default. Use [assets/ARCHITECTURE-PROFILE-TEMPLATE.md](assets/ARCHITECTURE-PROFILE-TEMPLATE.md) as its structure.

If the user explicitly requests an ADR, use the repository ADR directory and naming convention. Create a focused ADR for one decision.

If an existing profile uses another path, update it in place. Do not create a competing profile.

Ask a question only when an unresolved choice materially changes the record. Otherwise, put the choice under `Open decisions`.

## Create or update a profile

Record these items when they apply:

- The base architecture skill.
- The project scope.
- The selected API runtime and public API style.
- The selected identity and session approach.
- The authoritative server data store.
- The local data store and offline level.
- The AI provider boundary and routing policy.
- The AI stream, history, and context policies.
- Optional Cloudflare services that the project uses now.
- Project constraints and deliberate deviations.
- Links to product requirements, OpenAPI, schemas, and ADRs.
- Open decisions.

Keep each selection concise. Link to project details instead of duplicating them.

Delete unused template rows and all bracketed prompts. Do not invent a project choice from a generic default.

Use `Not selected` or move the item to `Open decisions` when the project lacks a decision. Do not hide uncertainty.

Do not copy generic security rules, REST conventions, stream events, or service descriptions into the profile.

## Maintain the documentation index

After you create or update the profile, create or update `docs/README.md`.

If the README does not exist, create this small index:

```md
# Project Documentation

## Architecture

- [Architecture profile](architecture-profile.md)
```

If the README exists, preserve its unrelated content. Add an `Architecture` section when it does not have one.

Keep one relative link to the profile in that section. Update an existing profile link instead of adding another link.

Adjust the relative link when the profile uses a non-default path.

If the user migrates generic architecture documents to the base skill, remove their links from the README. Do not remove other project-document links.

If the README only indexes those generic documents, replace its content with the small index above. Do not delete the generic documents.

Add an ADR index link only when the target exists. Do not create placeholder links.

## Create an ADR

Follow the repository ADR template when one exists. Otherwise, include:

- Status.
- Context.
- Decision.
- Alternatives.
- Consequences.
- Links to the project profile and relevant architecture-skill references.

An ADR records one durable decision. It does not replace the project profile.

## Preserve instruction boundaries

Do not edit `AGENTS.md` unless the user requests persistent agent guidance. Suggest `$sync-project-skill-guidance` when the architecture skill needs a durable pointer.

Do not delete generic project documents during profile creation. Remove or migrate them only when the user explicitly requests that work.

## Validate

Make sure that:

- The record names `$cloudflare-ios-api-architecture` as its base.
- Every selected option has repository evidence or user approval.
- Each deviation states its reason and affected scope.
- Every relative Markdown link resolves.
- No bracketed prompt remains.
- The record contains no copied generic architecture section.
- For profile work, `docs/README.md` contains one valid link to the profile.
- Existing project guidance outside the target file stays unchanged.

## Finish

For profile work, report the profile path and the documentation-index path.

Report the selected options, deviations, and open decisions.
