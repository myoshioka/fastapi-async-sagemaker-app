from fastapi import FastAPI
from time import sleep
import uvicorn
from datetime import datetime

app = FastAPI()


@app.get('/ping')
async def ping():
    return {"message": "ok"}


@app.post('/invocations')
async def invocations():
    print(f"{datetime.now():%H:%M:%S} sleep start.")
    sleep(5)
    print(f"{datetime.now():%H:%M:%S} sleep end.")
    return {"message": "finish"}


if __name__ == '__main__':
    uvicorn.run('sagemaker_endpoint:app',
                host='0.0.0.0',
                port=8080,
                log_level='info')
