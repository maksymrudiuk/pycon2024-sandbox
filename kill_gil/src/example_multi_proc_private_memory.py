import os
import sys
import multiprocessing
import time

from conf import TARGET


num_processes = os.cpu_count()


def cpu_bound_task(num):
    counter = 0
    for _ in range(num):
        counter += 1
    return counter


if __name__ == '__main__':
    start_time = time.time()

    print("Debug Info")
    print("is_gil_enabled: ", sys._is_gil_enabled())
    print("num_processes: ", num_processes)

    work_per_process = TARGET // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        counters = pool.map(cpu_bound_task, [work_per_process] * num_processes)

    counter = sum(counters)

    print(f"--- {time.time() - start_time} seconds ---")
    print("Counter: ", counter)