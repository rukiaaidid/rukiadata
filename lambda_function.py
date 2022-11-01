import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
   id = event['id']
   Question 1 = event['Question 1']
   Question 2 = event['Question 1']
   Question 3 = event['Question 1']
   Question 4 = event['Question 1']
   Question 5 = event['Question 1']
   Question 6 = event['Question 1']
   Question 7 = event['Question 1']
   dynamodb.put_item(TableName='test-table', Item={
      'Question 1':{'S':Question1}, 'Question 2':{'S':Question2},'Question 3':{'S':Question3},
      'Question 4':{'S':Question4},'Question 5':{'S':Question5},'Question 6':{'S':Question6},
      'Question 7':{'S':Question7}})
