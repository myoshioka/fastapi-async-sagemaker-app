import aiohttp
import asyncio

# URL = 'http://localhost:3000'
URL = 'http://localhost:3000/async'


async def fetch(session, url):
    print('call fetch')
    async with session.get(url) as response:
        r_text = await response.text()
        print('finished')
        return r_text


async def main(id):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, URL)
        print('count:{count} data:{data}'.format(count=id, data=response))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(main(1), main(2), main(3), main(4), main(5))
    # gather = asyncio.wait([main(1), main(2), main(3), main(4), main(5)])

    loop.run_until_complete(gather)
