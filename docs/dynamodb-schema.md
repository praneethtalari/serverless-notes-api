# DynamoDB Table Schema – Notes Application

## Table Name
`notes`

## Primary Key
- **Partition Key:** `note_id` (String, UUID)

## Attributes
| Attribute   | Type   | Description                          |
|-------------|--------|--------------------------------------|
| note_id     | String | UUID generated for each new note     |
| title       | String | Title of the note                    |
| body        | String | Content of the note                  |
| created_at  | String | ISO timestamp the note was created   |

## Example Item
```json
{
  "note_id": "uuid-1234",
  "title": "My First Note",
  "body": "This is a test note",
  "created_at": "2025-01-01T12:00:00Z"
}
