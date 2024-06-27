import time
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    # Create an aiohttp ClientSession
    async with aiohttp.ClientSession() as session:
        # Define the URLs to fetch
        urls = [
            "https://api.publicapis.org/entries",
            "https://www.boredapi.com/api/activity",
            "https://api.coindesk.com/v1/bpi/currentprice.json",
            "https://api.agify.io?name=meelad",
        ]

        # Create a list of coroutines for making requests
        coroutines = [fetch(session, url) for url in urls]

        # Execute the coroutines concurrently using asyncio.gather()
        responses = await asyncio.gather(*coroutines)

        # Process the responses
        for url, response in zip(urls, responses):
            print(f"Response from {url} is: {response[:20]}")

if __name__ == "__main__":
    start = time.perf_counter()
    # Run the main coroutine
    asyncio.run(main())
    end = time.perf_counter()

    print(f"Finished in {round(end - start, 2)} seconds")