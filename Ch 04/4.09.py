import asyncio
from aiohttp import ClientSession
from util import fetch_status, async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, "https://www.example.com", 1),
                    fetch_status(session, "https://www.example.com", 5),
                    fetch_status(session, "https://www.example.com", 4)]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("TimeOut!")

        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())
