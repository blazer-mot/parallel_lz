import asyncio
import time

async def async_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} завершилась через {delay} секунд.")

async def async_tasks():
    tasks = [
        asyncio.create_task(async_task("А", 1)),
        asyncio.create_task(async_task("Б", 2)),
        asyncio.create_task(async_task("В", 3)),
        asyncio.create_task(async_task("Г", 4)),
        asyncio.create_task(async_task("Д", 5))
    ]
    start = time.time()
    await asyncio.gather(*tasks)
    thread_time = time.time() - start
    print(f"Асинхронное выполнение заняло {thread_time:} секунд.")

def sync_tasks():
    start = time.time()
    for name, n in [("А", 1), ("Б", 2), ("В", 3), ("Г", 4), ("Д", 5)]:
        time.sleep(n)
        print(f"Задача {name} завершилась через {n} секунд.")
    thread_time = time.time() - start
    print(f"Последовательное выполнение заняло {thread_time:} секунд.")
