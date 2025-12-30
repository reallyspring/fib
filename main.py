import time
import logging
import functools

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@functools.lru_cache(maxsize=None)
def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

def time_call(func, *args, repeats=1):
    start = time.perf_counter()
    result = None
    for _ in range(repeats):
        result = func(*args)
    end = time.perf_counter()
    return result, end - start

n = 50

fib_i, t_i = time_call(fib_iter, n)
logging.info(f"Итеративная Фибоначчи({n}) = {fib_i}")
logging.info(f"Время работы (итеративно): {t_i:.8f} сек")

fib_r, t_r = time_call(fib_rec, n)
logging.info(f"Рекурсивная Фибоначчи({n}) = {fib_r}")
logging.info(f"Время работы (рекурсивно, с мемоизацией): {t_r:.8f} сек")

if t_r > 0:
    logging.info(f"Соотношение времени (рекурсив/итератив): {t_r / t_i if t_i>0 else float('inf'):.2f}")
else:
    logging.info("Рекурсивное время слишком мало для деления (практически 0).")


def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            if isinstance(item, (int, float)):
                total += item
            else:
                raise TypeError(f"Недопустимый элемент в списке: {item!r}")
    return total

data = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
result = recursive_sum(data)
print("Сумма элементов списка:", result)
