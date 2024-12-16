import os
import sys
import multiprocessing
import time

from conf import TARGET


num_processes = os.cpu_count()


def cpu_bound_task(counter, num):
    for _ in range(num):
        counter.value += 1


if __name__ == '__main__':
    start_time = time.time()

    print("Debug Info")
    print("is_gil_enabled: ", sys._is_gil_enabled())
    print("num_processes: ", num_processes)

    counter = multiprocessing.Value('i', 0)

    processes = [
        multiprocessing.Process(target=cpu_bound_task, args=(counter, TARGET // num_processes))
        for _ in range(num_processes)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Counter: ", counter.value)
    print(f"--- {time.time() - start_time} seconds ---")