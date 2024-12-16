import os
import sys
import time

from conf import TARGET


num_threads = os.cpu_count()


def cpu_bound_task(num):
    counter = 0
    for _ in range(num):
        counter += 1
    return counter



if __name__ == '__main__':
    start_time = time.time()

    print("Debug Info")
    print("is_gil_enabled: ", sys._is_gil_enabled())
    print("num_threads: ", num_threads)

    counter = cpu_bound_task(TARGET)

    print(f"--- {time.time() - start_time} seconds ---")

    print("Counter: ", counter)