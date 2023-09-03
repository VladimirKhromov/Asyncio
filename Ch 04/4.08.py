import asyncio
from aiohttp import ClientSession
from util import fetch_status, async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, "https://www.example.com", 1),
                    fetch_status(session, "https://www.example.com", 1),
                    fetch_status(session, "https://www.example.com", 4)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

asyncio.run(main())
