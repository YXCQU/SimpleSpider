import asyncio
import aiohttp
import time

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = 'http://111.231.227.238:8000'
    print('Waiting for', url)
    result = await get(url)
    # print('Get response from', url, 'Result:', result)


tasks = [asyncio.ensure_future(request()) for _ in range(500)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
