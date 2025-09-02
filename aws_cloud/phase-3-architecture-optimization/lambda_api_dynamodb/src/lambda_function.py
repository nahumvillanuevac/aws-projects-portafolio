import json
import boto3
import uuid
from datetime import datetime

# Connect to DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactForm')  # Make sure your table name matches

def lambda_handler(event, context):
    # Determine HTTP method
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    
    # CORS headers
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
    }

    # Handle preflight OPTIONS request
    if method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"status": "ok"})
        }

    try:
        # Parse POST body
        body = json.loads(event['body'])
        name = body.get("name")
        email = body.get("email")
        message = body.get("message")

        # Create item
        item = {
            "id": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "message": message,
            "createdAt": datetime.utcnow().isoformat()
        }

        # Save to DynamoDB
        table.put_item(Item=item)

        # Return success response
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"status": "saved", "data": item})
        }

    except Exception as e:
        # Return error response with headers
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }
