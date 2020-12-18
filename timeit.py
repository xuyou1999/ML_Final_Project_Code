import time

from simulation import simulate


def timeit(f, *args, **kwargs):
    start = time.perf_counter()
    f()
    finish = time.perf_counter()
    return finish - start


if __name__ == '__main__':
    print(timeit(simulate, "well", key="worst"))