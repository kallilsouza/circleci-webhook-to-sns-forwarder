# CircleCI Webhook to SNS Forwarder 

This repository contains an AWS Lambda function designed to process webhook events from CircleCI. It verifies the event's authenticity using a signature-based validation and then forwards the event to an Amazon SNS (Simple Notification Service) topic. The SNS topic can be further configured to relay these events, for example, to a Telegram bot for notifications.

## Features 
 
- **Signature Verification** : Ensures events are from CircleCI by validating the signature using an HMAC-SHA256 hash.
 
- **SNS Integration** : Publishes valid events to a pre-configured SNS topic.
 
- **Secure Configuration** : Utilizes environment variables to store sensitive information like the CircleCI secret and SNS Topic ARN.


---


## Requirements 
 
- **AWS Services** :
  - AWS Lambda

  - AWS SNS
 
- **Environment Variables** : 
  - `CIRCLECI_SECRET`: The secret key shared between CircleCI and this function for signature verification.
 
  - `SNS_TOPIC_ARN`: The ARN of the SNS topic where the events will be published.
 
- **Dependencies** : 
  - `boto3`: AWS SDK for Python


---


## How It Works 
 
1. **Webhook Event** : CircleCI sends a webhook payload to the configured endpoint.
 
2. **Signature Verification** : 
  - The function retrieves the `circleci-signature` header from the incoming event.
 
  - It validates the signature using the `CIRCLECI_SECRET` and the event payload.
 
3. **SNS Publishing** :
  - If the signature is valid, the event payload is published to the specified SNS topic.

  - The SNS topic can trigger downstream systems like a Telegram bot.
 
4. **Response** : 
  - `204 No Content` is returned if the process is successful.
 
  - `401 Unauthorized` is returned for invalid signatures.
 
  - `400 Bad Request` is returned if the request body is empty.


---


## Setup 

### Prerequisites 
 
1. **AWS Account** :
  - Create an SNS topic and note its ARN.

  - Configure an IAM role for the Lambda function with permissions to publish to the SNS topic.
 
2. **CircleCI** :
  - Set up a webhook in CircleCI pointing to the Lambda function's API Gateway endpoint.
 
3. **AWS Lambda Deployment** :
  - Package the Python code and dependencies into a zip file.

  - Deploy the Lambda function using AWS CLI, AWS Management Console, or an infrastructure-as-code tool like Terraform.


---


### Environment Variables 

Add the following environment variables in your Lambda function configuration:
| Variable | Description | 
| --- | --- | 
| CIRCLECI_SECRET | The secret shared with CircleCI for signature verification. | 
| SNS_TOPIC_ARN | The ARN of the SNS topic to forward the events to. | 


---
