from fastapi import FastAPI
from time import sleep
import uvicorn

app = FastAPI()


@app.get('/ping')
def ping():
    return {"message": "ok"}


@app.post('/invocations')
def invocations():
    sleep(5)
    return {"message": "finish"}


if __name__ == '__main__':
    uvicorn.run('sagemaker_endpoint:app',
                host='0.0.0.0',
                port=8080,
                log_level='info')
