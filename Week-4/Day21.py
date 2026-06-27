# Mini Project — Async Multi-API Fetcher
# n Async script fetching IN PARALLEL:
# n 1. Weather for your city
# n 2. Random quote
# n 3. News headline
# n Print formatted briefing
# n This is Jarvis morning briefing v0.0!

import asyncio
import feedparser
import httpx
import pytest

async def get_weather(session: httpx.AsyncClient, city: str) -> str:
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = await session.get(url, timeout=5)  # don't wait forever
        response.raise_for_status()  # raise exception for HTTP errors
        return response.text.strip()
    except httpx.RequestError as e:
        return f"Error fetching weather: {e}"
    except httpx.HTTPStatusError as e:
        return f"HTTP error fetching weather: {e}"

def format_quote(quote, author):
    return f"{quote} — {author}"

async def get_quote(session: httpx.AsyncClient) -> str:
    url = "https://zenquotes.io/api/random"
    try:
        response = await session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return format_quote(data[0]['q'], data[0]['a'])
    except httpx.RequestError as e:
        return f"Error fetching quote: {e}"
    except httpx.HTTPStatusError as e:
        return f"HTTP error fetching quote: {e}"
    
async def get_news(session: httpx.AsyncClient) -> str:
    url = "https://feeds.bbci.co.uk/news/world/rss.xml"
    headers = {"User-Agent": "JarvisMorningBriefing/0.0"}
    try:
        response = await session.get(url, timeout=5)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        top_story = feed.entries[0].title
        return f"Top news: {top_story} (BBC World)"
    except httpx.RequestError as e:
        return f"Error fetching news: {e}"
    except httpx.HTTPStatusError as e:
        return f"HTTP error fetching news: {e}"
    
async def main(cities: list[str]):
    async with httpx.AsyncClient() as session:
        weather_tasks = [get_weather(session, city) for city in cities]
        quote_task = get_quote(session)
        news_task = get_news(session)
        
        results = await asyncio.gather(*weather_tasks, quote_task, news_task)
        
        print("\n--- Jarvis Morning Briefing ---")
        for result in results:
            print(result)

def test_format_quote():
    result = format_quote("Life is short", "Buddha")
    assert result == "Life is short — Buddha"


if __name__ == "__main__":
    asyncio.run(main([input("Enter a city for weather: ")]))
    
