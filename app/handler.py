import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")

def lambda_handler(event, context):
    try:
        method = event.get("requestContext", {}).get("http", {}).get("method")
        path_params = event.get("pathParameters") or {}
        note_id = path_params.get("note_id")

        if method == "POST":
            body = json.loads(event["body"])
            note_id = str(uuid.uuid4())
            item = {
                "note_id": note_id,
                "title": body.get("title", ""),
                "body": body.get("body", ""),
                "created_at": datetime.utcnow().isoformat()
            }
            table.put_item(Item=item)
            return respond(201, item)

        elif method == "GET" and note_id:
            response = table.get_item(Key={"note_id": note_id})
            item = response.get("Item")
            if item:
                return respond(200, item)
            else:
                return respond(404, {"error": "Note not found"})

        elif method == "GET":
            response = table.scan()
            return respond(200, response.get("Items", []))

        elif method == "PUT" and note_id:
            body = json.loads(event["body"])
            table.update_item(
                Key={"note_id": note_id},
                UpdateExpression="SET title = :t, body = :b",
                ExpressionAttributeValues={
                    ":t": body.get("title", ""),
                    ":b": body.get("body", "")
                }
            )
            return respond(200, {"message": "Note updated", "note_id": note_id})

        elif method == "DELETE" and note_id:
            table.delete_item(Key={"note_id": note_id})
            return respond(200, {"message": "Note deleted", "note_id": note_id})

        else:
            return respond(400, {"error": "Unsupported method or missing note_id"})

    except Exception as e:
        print(f"Error: {str(e)}")
        return respond(500, {"error": "Internal Server Error"})

def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
