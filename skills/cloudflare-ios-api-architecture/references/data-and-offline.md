# Data and Offline Behavior

## Data ownership

The API is the source of truth for synchronized application data. Cloudflare D1 stores relational data that the API owns.

The iOS app stores a local copy for fast startup, local queries, drafts, and limited offline work. SwiftData is the reference local store.

The local copy does not become a second cloud authority. The Worker resolves all accepted server changes and access decisions.

## Data categories

| Data category | Authoritative store | iOS storage |
|---|---|---|
| Application records | API and D1 | SwiftData cache |
| Pending offline changes | iOS outbox until acceptance | SwiftData |
| Draft text and interface state | iOS app | SwiftData |
| Application session | Session service | Keychain token |
| Large files | API and object storage | Optional file cache |
| AI conversation state | API when server history is enabled | Optional SwiftData cache |

## Model boundaries

Keep the iOS model and D1 schema independent. Use versioned API data-transfer objects between them.

```text
SwiftData model <-> API object <-> D1 row
```

This boundary lets the local model and server schema change at different times. It also prevents persistence details from becoming the API contract.

Each synchronized record uses a stable application identifier. Do not use a SwiftData `PersistentIdentifier` as a server identifier.

A synchronized record usually includes these fields:

```text
id
revision
createdAt
updatedAt
deletedAt
```

The exact fields depend on the record and its conflict policy.

## Fast app startup

The app reads permitted cached data before the first network response. This behavior makes app startup independent of normal API latency.

The app marks cached data with its last successful synchronization time. The interface can show stale or offline state when that information matters.

After startup, the app requests server changes. The app applies the response to SwiftData and then updates the synchronization cursor.

## Offline levels

The architecture supports two offline levels.

### Cache and drafts

This level is the default. The app reads cached records and stores local drafts while the network is unavailable.

The app does not change shared server records offline. It sends the draft after the user submits it and the network returns.

### Offline changes

Use this level only when a product requires offline changes to synchronized records.

The app stores each change in an outbox. Each outbox item has a unique mutation identifier and its last known server revision.

The Worker validates the session, authorization, mutation identifier, and revision. It applies each accepted mutation once.

## Outbox flow

1. Change the local record.
2. Add the matching mutation to the outbox.
3. Save the record and mutation in one local transaction.
4. Update the interface from SwiftData.
5. Send the mutation when network access is available.
6. Validate the mutation in the Worker.
7. Apply the accepted change to D1.
8. Return the server revision.
9. Remove the acknowledged mutation from the outbox.

The app keeps an unacknowledged mutation after a network failure. A retry uses the same mutation identifier.

## Incremental server changes

The server returns authorized changes after a server-generated cursor. The client clock is not a synchronization cursor.

The response contains a limited page and the next cursor. The app stores the new cursor only after it saves all page changes.

Deleted records use tombstones when clients must learn about deletions. The retention policy defines how long the server keeps each tombstone.

## Conflicts

Each writable record type has an explicit conflict policy. The Worker rejects a stale revision when automatic replacement can lose valid data.

The API can return `409 Conflict` with the current server record. The app then displays, merges, or retries according to product policy.

Do not apply one conflict rule to all data types. A status value, free-form document, and financial record require different rules.

## Large data

D1 stores structured records and metadata. Object storage holds photos, documents, recordings, and other large objects.

The D1 record stores the object key, authorization scope, media type, size, and checksum. The Worker authorizes each object operation.

Do not copy vendor limits into this architecture. Read the current [D1 limits](https://developers.cloudflare.com/d1/platform/limits/) before implementation.

## Related documents

- [System overview](system-overview.md)
- [Authentication and security](authentication-and-security.md)
- [Application API](application-api.md)
- [AI context](ai-context.md)
- [Operations and evolution](operations-and-evolution.md)
