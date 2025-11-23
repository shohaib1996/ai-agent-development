# import asyncio


# async def say_hello():
#     await asyncio.sleep(10)
#     print("Hello!")


# asyncio.run(say_hello())

import asyncio


# async def task_1():
#     await asyncio.sleep(1)
#     return "Task 1 done"


# async def task_2():
#     await asyncio.sleep(5)
#     return "Task 2 done"


# async def main():
#     results = await asyncio.gather(task_1(), task_2())
#     print(results)


# asyncio.run(main())

# import httpx


# async def fetch_posts():
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://jsonplaceholder.typicode.com/posts")
#         return r.json()


# async def main():
#     posts = await fetch_posts()
#     print(posts[0]["title"])  # access first post


# asyncio.run(main())

# import httpx


# async def fetch_quote():
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://api.quotable.io/random")
#         data = r.json()
#         return {"content": data["content"], "author": data["author"]}


# async def main():
#     tasks = [fetch_quote(), fetch_quote(), fetch_quote()]
#     results = await asyncio.gather(*tasks)

#     for i, quote in enumerate(results, start=1):
#         print(f"\nQuote {i}:")
#         print(quote["content"])
#         print("–", quote["author"])


# asyncio.run(main())
import aiohttp
import random


async def fetch_post(session):
    post_id = random.randint(1, 100)
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with session.get(url) as r:
        return await r.json()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post(session) for _ in range(3)]
        results = await asyncio.gather(*tasks)

        for post in results:
            print(f"{post['id']}: {post['title']}")


asyncio.run(main())
