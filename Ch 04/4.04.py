import asyncio

from util import async_timed, delay


# НЕПРАВИЛЬНОЕ использование спискового включения для создания и ожидания задач

@async_timed()
async def main():
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())

# Здесь применяется await сразу же после создания задачи, в связи с этим
# мы останавливаем работу list comprehension
