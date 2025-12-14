import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")

def lambda_handler(event, context):
    try:
        method = event.get("requestContext", {}).get("http", {}).get("method")

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

        elif method == "GET":
            response = table.scan()
            return respond(200, response.get("Items", []))

        elif method == "PUT":
            body = json.loads(event["body"])
            note_id = body.get("note_id")
            if not note_id:
                return respond(400, {"error": "note_id required in body"})
            table.update_item(
                Key={"note_id": note_id},
                UpdateExpression="SET title = :t, body = :b",
                ExpressionAttributeValues={
                    ":t": body.get("title", ""),
                    ":b": body.get("body", "")
                }
            )
            return respond(200, {"message": "Note updated", "note_id": note_id})

        elif method == "DELETE":
            body = json.loads(event["body"])
            note_id = body.get("note_id")
            if not note_id:
                return respond(400, {"error": "note_id required in body"})
            table.delete_item(Key={"note_id": note_id})
            return respond(200, {"message": "Note deleted", "note_id": note_id})

        else:
            return respond(400, {"error": "Unsupported method"})

    except Exception as e:
        print(f"Error: {str(e)}")
        return respond(500, {"error": "Internal Server Error"})

def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
