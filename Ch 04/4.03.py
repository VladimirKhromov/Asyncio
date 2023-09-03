import asyncio

import aiohttp
from aiohttp import ClientSession
from aiohttp import ClientTimeout


# Тайм-аут задается с помощью структуры данных aiohttp.ClientTimeout
# Она позволяет не только общий тайм-аут в секундах для всего запроса, но и отдельные
# Для установления соединения или чтения данных

async def fetch_status(session: ClientSession, url: str) -> int:
    # .01 Не хватает для подключения, будет ошибка asyncio.TimeoutError
    ten_millis = ClientTimeout(total=.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, "https://www.example.com")


asyncio.run(main())
