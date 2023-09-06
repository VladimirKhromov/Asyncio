# Создания пула процессов c асинхронным получением результатов
from multiprocessing import Pool


# from time import sleep


def say_hello(name: str) -> str:
    # sleep(1)
    return f'Привет, {name}'


if __name__ == "__main__":
    # apply_async запускает оба вызова в отдельных процессах
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=("Jeff",))
        hi_john = process_pool.apply_async(say_hello, args=("John",))
        print(hi_jeff.get())
        print(hi_john.get())

# минус - при разной скорости работы процессов
# мы увидим результат после обработки всех процессов
