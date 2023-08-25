import asyncio
from asyncio import shield

from util import delay
# 59

async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task
        print(result)


asyncio.run(main())
