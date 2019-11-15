import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo_test')

def get_person(id):
    response = table.get_item(
            Key={
                 'test_id': id
            }
        )
    return response['Item']

def lambda_handler(event, context):
    try:
        return get_person(event['test_id'])
    except Exception as e:
        return get_person('?')