import asyncio
import time

from conf import TARGET

num_tasks = 4


async def cpu_bound_task(num):
    counter = 0
    for _ in range(num):
        counter += 1
    return counter

async def main():
    start_time = time.time()

    print("Debug Info")
    print("num_tasks: ", num_tasks)

    work_per_task = TARGET // num_tasks

    tasks = [cpu_bound_task(work_per_task) for _ in range(num_tasks)]

    counters = await asyncio.gather(*tasks)

    total_counter = sum(counters)

    print("Counter: ", total_counter)
    print(f"--- {time.time() - start_time} seconds ---")

# Run the main event loop
if __name__ == '__main__':
    asyncio.run(main())