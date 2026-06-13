# Async/Await Basics
# n import asyncio
# n async def fetch(): await something()
# n asyncio.run(main())
# n asyncio.gather() — parallel tasks
# n pip install aiohttp
# n Async fetch: 3 cities simultaneously

import asyncio
import httpx

# Step 1: write an async function that fetches weather for ONE city
async def get_weather(session, city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = await session.get(url, timeout=5)  # don't wait forever
        response.raise_for_status()                    # crash if 4xx or 5xx
        return response.text
    except httpx.TimeoutException:
        return f"{city}: ❌ request timed out"
    except httpx.HTTPStatusError:
        return f"{city}: ❌ city not found"
    except httpx.RequestError:
        return f"{city}: ❌ network error"

# Step 2: write the main function that fetches ALL cities at once
async def main(cities):
    async with httpx.AsyncClient() as session:
        results = await asyncio.gather(*[get_weather(session, city) for city in cities])
        for result in results:
            print(result)

cities = input("Enter cities separated by commas: ")
cities = [city.strip() for city in cities.split(",")]

asyncio.run(main(cities))