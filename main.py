from potoki_1 import posled, potok
from process_2 import kvadr
from asinxron_3 import async_tasks, sync_tasks
import asyncio

async def main():
    first_1 = posled()
    first_2 = potok()
    second = kvadr()
    third_1 = await async_tasks()
    third_2 = sync_tasks()
    
if __name__ == "__main__":
    asyncio.run(main()) 


