import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
  firstName = event['firstName']
  email = event['email']
  message = event['message']
  dynamodb.put_item(TableName='test-table', Item=
{'name':{'S':name},'email':{'S':email}, 'message':{'S':message}})
  print(email)
   
