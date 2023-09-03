import asyncio
import logging
import aiohttp
from util import fetch_status

async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, "https://www.example.com")
        bad_request = fetch_status(session, "python://www.example.com")

        fetchers = [asyncio.create_task(good_request),
                    asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихзся задач: {len(done)}")
        print(f"Число ожиюающих задач: {len(pending)}")

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=done_task.exception())

asyncio.run(main())
