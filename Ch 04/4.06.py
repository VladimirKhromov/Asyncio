import asyncio

from aiohttp import ClientSession

from util import fetch_status, async_timed

# Конкурентное выполнение запросов с помощью gather
@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]
        # Сгенерировать список сопрограм для каждого запроса
        requests = [fetch_status(session, url) for url in urls]
        # Ждать завершения всех запросов
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
