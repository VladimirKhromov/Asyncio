import asyncio

from util import async_timed, delay

@async_timed()
async def main():
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]

asyncio.run(main())

# Здесь 2 раза создаем list comprehension. Первый для создания задач.
# Второй для ожидания их выполнения
#
# Но и тут 3 недостатка. Первый это как раз два списка, второй - негибкость,
# мы ждем завершения работы программы. Третий - нет обработки исключений
