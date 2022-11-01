import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
   Question_1 = event['Question 1']
   Question_2 = event['Question 2']
   Question_3 = event['Question 3']
   Question_4 = event['Question 4']
   Question_5 = event['Question 5']
   Question_6 = event['Question 6']
   Question_7 = event['Question 7']
   dynamodb.put_item(TableName='test-table', Item={
      'Question 1':{'S':Question1}, 'Question 2':{'S':Question2},'Question 3':{'S':Question3},
      'Question 4':{'S':Question4},'Question 5':{'S':Question5},'Question 6':{'S':Question6},
      'Question 7':{'S':Question7}})
   
