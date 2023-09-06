import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(data: List, chunk_size: int) -> List:
    """ Разбить список data на части размером chunk_size. """
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    """
    Функция анализирует список строк chunk и создает словать,
    в котором слова являются ключами, а их частоты - значениями.
    На вход подается файл со строками типа "A'Aang_NOUN 1975 4 1"
    """
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        counter[word] = counter[word] + int(count) if counter.get(word) else int(count)
    return counter


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merge = first
    for key in second:
        merge[key] = merge[key] + second[key] if key in merge else second[key]
    return merge


async def main(partition_size: int):
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                # Для каждой порции выполнять операцию отображения в отдельном процессе
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            # Ждать завершения всех операций отображения
            intermediate_results = await asyncio.gather(*tasks)
            # Редуцировать промежуточные результаты в окончательный
            final_result = functools.reduce(merge_dictionaries, intermediate_results)

            print(f"Aardvark встречается {final_result['Aardvark']} раз.")

            end = time.time()
            print(f'Время MapReduce: {(end - start):.4f} секунд.')


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))

# partition_size=90000 - Заняло 18,5 сек
# partition_size=60000 - Заняло 16,5 сек
