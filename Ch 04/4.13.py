import asyncio

import aiohttp

from util import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url))]

        # Сопрограмма wait вернет управление, как только завершится любой из них
        # когда return_when=asyncio.FIRST_COMPLETED
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f"Число завершившихзся задач: {len(done)}")
        print(f"Число ожиюающих задач: {len(pending)}")

        for done_task in done:
            print(await done_task)


asyncio.run(main())
