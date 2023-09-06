# Создания пула процессов
from multiprocessing import Pool
# from time import sleep


def say_hello(name: str) -> str:
    # sleep(1)
    return f'Привет, {name}'


if __name__ == "__main__":
    # создание пула процессов в контекстном менеджере
    # поскольку после работы нужно остановить созданные процессы
    with Pool() as process_pool:
        hi_jeff = process_pool.apply(say_hello, args=("Jeff",))
        hi_john = process_pool.apply(say_hello, args=("John",))
        print(hi_jeff)
        print(hi_john)

# Здеть метод apply блокирует выполнение, пока функция не завершиться.
