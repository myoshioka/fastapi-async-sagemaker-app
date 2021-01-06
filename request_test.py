import aiohttp
import asyncio
from datetime import datetime

URL = 'http://localhost:3000'


# URL = 'http://localhost:3000/async'
async def main(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            res_text = await response.text()
            return f"response:{res_text}  id:{id}"


if __name__ == '__main__':
    print(f"{datetime.now():%H:%M:%S} start")
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(main(1), main(2), main(3), main(4))
    results = loop.run_until_complete(gather)
    for r in results:
        print(f"result: {r}")
    print(f"{datetime.now():%H:%M:%S} end")
