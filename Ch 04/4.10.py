import asyncio
import aiohttp
from util import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = \
                    [
                        asyncio.create_task(fetch_status(session, "https://www.example.com")),
                        asyncio.create_task(fetch_status(session, "https://www.example.com")),
                    ]

        # Предложение await wait вернет управление, когда все запросы завершатся,
        # и мы получим два множества: завершившиеся задачи и еще работающие задачи.
        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихзся задач: {len(done)}")
        print(f"Число ожиюающих задач: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())
