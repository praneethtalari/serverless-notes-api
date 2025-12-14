import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("notes")

def lambda_handler(event, context):
    http_method = event["requestContext"]["http"]["method"]

    if http_method == "POST":
        body = json.loads(event["body"])

        note_id = str(uuid.uuid4())
        item = {
            "note_id": note_id,
            "title": body["title"],
            "body": body["body"],
            "created_at": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(item)
        }

    if http_method == "GET":
        response = table.scan()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response["Items"])
        }

    return {
        "statusCode": 400,
        "body": "Unsupported method"
    }
