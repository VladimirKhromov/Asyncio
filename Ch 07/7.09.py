from threading import RLock, Thread

list_lock = RLock()

def sum_list(int_list: list[int]) -> int:
    print('Ожидание блокировки...')
    with list_lock:
        print('Блокировка захвачена.')
        if len(int_list) == 0:
            print('Cуммирование завершеною')
            return 0
        else:
            head, *tail = int_list
            print("Суммируется остаток списка")
            return head + sum_list(tail)

thread = Thread(target=sum_list, args=([1,2,3,4],))
thread.start()
thread.join()