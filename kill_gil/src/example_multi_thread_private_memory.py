import os
import sys
import threading
import time

from conf import TARGET


num_threads = os.cpu_count()


def cpu_bound_task(counter, num):
    for _ in range(num):
        counter["value"] += 1


counters = [{"value": 0} for _ in range(num_threads)]
threads = [
    threading.Thread(target=cpu_bound_task, args=(counter, TARGET // num_threads))
    for counter in counters
]


if __name__ == '__main__':
    start_time = time.time()

    print("Debug Info")
    print("is_gil_enabled: ", sys._is_gil_enabled())
    print("num_threads: ", num_threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    counter = sum(counter["value"] for counter in counters)

    print("Counter: ", counter)
    print(f"--- {time.time() - start_time} seconds ---")