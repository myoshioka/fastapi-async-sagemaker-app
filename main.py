import os
from fastapi import FastAPI, HTTPException
import uvicorn
import boto3
import json
import aiobotocore

app = FastAPI()
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']


@app.get('/async')
async def index_async():
    print('receive requests')
    try:
        session = aiobotocore.get_session()
        async with session.create_client('sagemaker-runtime') as client:
            sagemaker_response = await client.invoke_endpoint(
                EndpointName=ENDPOINT_NAME,
                Accept='application/json',
                ContentType='application/json',
                Body=json.dumps({'message': 'test'}))
            response_body = sagemaker_response['Body']
            async with response_body as stream:
                data = await stream.read()
                return json.loads(data.decode())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,
                            detail='Sagemaker invoke endpoint exception')


@app.get('/')
async def index():
    print('receive requests')

    try:
        sagemaker = boto3.client('sagemaker-runtime')
        sagemaker_response = sagemaker.invoke_endpoint(
            EndpointName='sagemaker-endpoint-test',
            Accept='application/json',
            ContentType='application/json',
            Body=json.dumps({'message': 'test'}))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,
                            detail='Sagemaker invoke endpoint exception')

    response_body = sagemaker_response['Body']
    return json.load(response_body)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=3000, log_level='info')
