import asyncio

async def task1():
    print("Executing task 1...")
    await asyncio.sleep(3)
    print("Task 1 completed.")

async def task2():
    print("Executing task 2...")
    await asyncio.sleep(1)
    print("Task 2 completed.")

async def task3():
    print("Executing task 3...")
    await asyncio.sleep(2)
    print("Task 3 completed.")

async def main():
    # Create a list of tasks
    tasks = [task1(), task2(), task3()]

    # Gather and concurrently execute the tasks
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())