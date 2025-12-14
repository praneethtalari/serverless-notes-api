resource "aws_dynamodb_table" "notes" {
  name         = "notes"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "note_id"

  attribute {
    name = "note_id"
    type = "S"
  }
}
