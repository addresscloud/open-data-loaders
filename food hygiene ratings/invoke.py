import boto3, json, pandas

lambda_client = boto3.client('lambda')

request = [{'query':'1 Bedford Grove' }]

lambda_payload = {
    'headers': { 
      'x-client-id': 'acdata',
    },
    'body': json.dumps(request),
    'pathParameters': { 'target': 'address' },
    'requestContext': {
      'httpMethod': 'POST',
      'authorizer': {
        'x-client-id': 'acdata',
      }
    }
  }

print(json.dumps(lambda_payload))

res = lambda_client.invoke(
    FunctionName='addresscloud-match_geocode-prod', 
    InvocationType='RequestResponse',
    Payload=json.dumps(lambda_payload)
    )

print(res['Payload'])
print(res['Payload'].read())
