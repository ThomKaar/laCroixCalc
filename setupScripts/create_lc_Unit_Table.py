# This file creates a table in DynamoDB that represents a single unit of LaCroix
# to be bought from a store
import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    AttributeDefinitions= [
        {
            'AttributeName': 'storeName',
            'AttributeType': 'S'
        },
        {
        	'AttributeName': 'price',
        	'AttributeType': 'N'
        }
    ],
    TableName='lc_Unit',
    KeySchema=[
    	{
            'AttributeName': 'storeName',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'price',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)