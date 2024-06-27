import asyncio
import httpx
import time

urls = [
    "https://httpbin.org/get",
    "https://api.publicapis.org/entries",
    "https://www.boredapi.com/api/activity",
    "https://api.coindesk.com/v1/bpi/currentprice.json",
    "https://api.agify.io?name=meelad",
]


async def main():
    tasks = []
    async with httpx.AsyncClient() as client:
        for url in urls:
            tasks.append(client.get(url))
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.status_code)

def fetch():
    with httpx.Client() as client:
        for url in urls:
            response = client.get(url)
            print(response.status_code)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"async finished in {round(end - start, 2)} seconds")
    start = time.perf_counter()
    fetch()
    end = time.perf_counter()
    print(f"sync finished in {round(end - start, 2)} seconds")