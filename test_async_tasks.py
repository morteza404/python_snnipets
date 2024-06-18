import asyncio
from time import perf_counter

async def say_hello():
    print("Hello!")
    await asyncio.sleep(3)
    print("123")

async def say_bye():
    print("bye!")
    await asyncio.sleep(1)
    print("456")

async def main():
    tasks = [say_hello(), say_bye()]    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Finished in {end - start:.2f} seconds")