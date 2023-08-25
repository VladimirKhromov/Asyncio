# Вычисление чисел Фибоначи

import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) равно {fib(number)}')


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.time()

fibs_no_threading()

end = time.time()

print(f'Время работы {end - start:.4f} с.')

# fib(40) равно 63245986
# fib(41) равно 102334155
# Время работы 33.1992 с.
