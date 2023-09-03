from aiohttp import ClientSession
from asyncio import sleep
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession,
                       url: str,
                       delay: int = 0) -> int:
    await sleep(delay)
    async with session.get(url) as result:
        return result.status