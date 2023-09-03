import asyncio

import aiohttp

from util import fetch_status
# Использование тайм-аутов в wai


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url, 3))]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f"Число завершившихзся задач: {len(done)}")
        print(f"Число ожиюающих задач: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())
