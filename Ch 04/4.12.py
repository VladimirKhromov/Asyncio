import asyncio
import logging
import aiohttp
from util import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, "bad://www.example.com"),
                    fetch_status(session, "https://www.example.com", 3),
                    fetch_status(session, "https://www.example.com", 3)]

        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихзся задач: {len(done)}")
        print(f"Число ожиюающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=done_task.exception())
        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())
