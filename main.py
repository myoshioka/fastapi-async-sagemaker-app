from fastapi import FastAPI
from time import sleep
import aiohttp
import uvicorn
# import asyncio
# import requests
# from fastapi import BackgroundTasks
# from datetime import datetime
# from asyncio import sleep

app = FastAPI()


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


@app.get('/')
async def index():
    print('receive requests')

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://api:3333/sleep')
        print(html)

    return {"text": "success"}


@app.get('/sleep')
async def sleepapp():
    sleep(5)
    return {"text": "finish"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=3000, log_level='info')
