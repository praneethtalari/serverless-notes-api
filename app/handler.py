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
            result = table.scan()
            items = result.get("Items", [])
            return respond(200, items)

     
        else:
            return respond(400, {"error": "Unsupported HTTP method"})

    except Exception as e:
        print(f"Error: {str(e)}")
        return respond(500, {"error": "Internal Server Error"})



def respond(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
        },
        "body": json.dumps(body)
    }

