import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


result = asyncio.run(coroutine_add_one(1))  # asyncio.run() точка входа в созданое приложение asyncio
print(result)
