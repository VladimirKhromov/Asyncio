from asyncio import Future

my_future = Future()

print(f'my_future готов? {my_future.done()}')

my_future.set_result(42)

print(f'my_future готов? {my_future.done()}')

print(f'какой результат храниться в my_future? {my_future.result()}')
