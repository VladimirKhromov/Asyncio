import asyncio

from util import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


asyncio.run(main())

# результат будет [3, 1] - в том порядке, в каком программы передавались.
# Функция gather гарантирует детерминированный порядок результатов, несмотря на
# недетерминированность их получения
