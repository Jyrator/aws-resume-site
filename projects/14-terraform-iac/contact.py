import json
import boto3

def handler(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1')

    try:
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        ses_client.send_email(
            Source="ejirosaks@gmail.com",
            Destination={'ToAddresses': ["ejirosaks@gmail.com"]},
            Message={
                'Subject': {'Data': f'Contact Form Submission from {name}'},
                'Body': {'Text': {'Data': f'From: {name} <{email}>\n\n{message}'}}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully!'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
