import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)
    print(one_plus_one, two_plus_one, end="\n")


asyncio.run(main())
