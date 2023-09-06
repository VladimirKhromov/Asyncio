from multiprocessing import Process, Value, cpu_count


def increment_value(shared_int: Value):
    shared_int.value = shared_int.value + 1


if __name__ == '__main__':
    print(cpu_count())
    for _ in range(10000):
        integer = Value('i', 0)
        procs = [Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 Process(target=increment_value, args=(integer,)),
                 ]

        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        # Пришлось увеличить количество процессов с 2 до 12, поскольку для 2 я бы не дождался assert'a :)
        assert(integer.value == 12)
