import threading
import time

import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


sync_start = time.time()
read_example()
read_example()
sync_end = time.time()
print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} с.')
print()


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)
print('Запускаем потоки!')
thread_start = time.time()
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
thread_end = time.time()
print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')

# 200
# 200
# Синхронное выполнение заняло 0.9938 с.
#
# Запускаем потоки!
# 200
# 200
# Многопоточное выполнение заняло 0.5070 с.
# В случае же ожидания ввода - вывода GIL освобождается, и в этом примере дает убыстрение почти в 2 раза.