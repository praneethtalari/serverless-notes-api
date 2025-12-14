import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")

def lambda_handler(event, context):
    try:
        http_method = event.get("requestContext", {}).get("http", {}).get("method")

        if http_method == "POST":
            if not event.get("body"):
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Missing request body"})
                }

            body = json.loads(event["body"])

            note_id = str(uuid.uuid4())
            item = {
                "note_id": note_id,
                "title": body.get("title", ""),
                "body": body.get("body", ""),
                "created_at": datetime.utcnow().isoformat()
            }

            table.put_item(Item=item)

            return {
                "statusCode": 201,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(item)
            }

        elif http_method == "GET":
            response = table.scan()
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(response.get("Items", []))
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Unsupported method"})
            }

    except Exception as e:
        # Log the error for CloudWatch
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
