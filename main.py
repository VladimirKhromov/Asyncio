import asyncio

async def task_with_delay(name, delay):
    if delay == 4:
        raise IndexError
    await asyncio.sleep(delay)
    return f"Task {name} completed after {delay} seconds"

async def main():
    tasks = [
        task_with_delay("A", 3),
        task_with_delay("B", 2),
        task_with_delay("C", 1),
        task_with_delay("D", 4),
    ]

    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            print(result)
        except IndexError:
            print("Error")

asyncio.run(main())