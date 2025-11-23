# import asyncio


# async def say_hello():
#     await asyncio.sleep(10)
#     print("Hello!")


# asyncio.run(say_hello())

import asyncio


async def task_1():
    await asyncio.sleep(1)
    return "Task 1 done"


async def task_2():
    await asyncio.sleep(5)
    return "Task 2 done"


async def main():
    results = await asyncio.gather(task_1(), task_2())
    print(results)


asyncio.run(main())
