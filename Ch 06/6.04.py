import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start}')
    return counter


if __name__ == "__main__":
    start_time = time.time()

    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 5, 22, 40000, 100000000, 200000000]
        for result in process_pool.map(count, numbers):
            print(result)

    end_time = time.time()
    print(f'Полное время работы {end_time - start_time}')

# минус здесь - порядок итераций определяется в каком порядке стоят числа в numbers,
# если бы первым числом был 100 000 000 то пришлось бы ждать
# заверщения этого вызова, прежде чем увидеть другие результаты
