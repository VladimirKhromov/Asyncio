import asyncio

import aiohttp

from util import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url))]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f"Число завершившихзся задач: {len(done)}")
            print(f"Число ожиюающих задач: {len(pending)}")

            for done_task in done:
                print(await done_task)


asyncio.run(main())
