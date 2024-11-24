import json
import boto3
import os

from validators import verify_signature

sns_client = boto3.client("sns")

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")


def lambda_handler(event, context):
    headers = event.get("headers", {})
    body = event.get("body")

    if not verify_signature(os.getenv("CIRCLECI_SECRET"), headers, body):
        return {"statusCode": 401}

    if not body:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No body in event"}),
        }

    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN, Message=body, Subject="Event Forwarded to SNS"
    )

    return {
        "statusCode": 204,
    }
