import time
from threading import Lock, Thread

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:  # Захватить блокировку
        print('Захвачена блокировка a из метода a!')
        time.sleep(1)  # Ждать 1 секунду, это создает подходящие условия для взаимоблокировки
        with lock_b:  # C
            print('Захвачены обе блокировки из метода а!')


def b():
    with lock_b:
        print('Захвачена блокировка b из метода b!')
        with lock_a:
            print('Захвачены обе блокировки из метода b!')


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
