# Async News Aggregator — fetches 5 different news sources in PARALLEL, deduplicates similar headlines, displays a clean digest.
# This is a real prototype of Jarvis news capability.
# n asyncio.gather() to fetch from 5 RSS feeds simultaneously
# n Use feedparser library for RSS parsing
# n Simple deduplication: if 80%+ word overlap, treat as same story
# n colorama for category colour coding
# n Save digest as markdown to digests/YYYY-MM-DD.md
# n BONUS: schedule with Windows Task Scheduler or cron

import asyncio

from colorama import Fore
from colorama import Fore
import feedparser
import httpx
import os



async def get_news(session: httpx.AsyncClient, url: str) -> str:
    headers = {"User-Agent": "JarvisNewsAggregator/0.0"}
    try:
        response = await session.get(url, timeout=5, headers=headers)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        if not feed.entries:
            return f"No news entries found for {url}"
        top_story = feed.entries[0].title
        return f"Top news: {top_story} ({url})"
    except httpx.RequestError as e:
        return f"Error fetching news from {url}: {e}"
    except httpx.HTTPStatusError as e:
        return f"HTTP error fetching news from {url}: {e}"
    
async def main(news_sources: list[str]):
    async with httpx.AsyncClient() as session:
        tasks = [get_news(session, url) for url in news_sources]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
        return results  # Return results for further processing (e.g., deduplication)

def deduplicate_headlines(headlines: list[str]) -> list[str]:
    """Deduplicate headlines based on 80% word overlap."""
    unique_headlines = []
    for headline in headlines:
        if not any(is_similar(headline, existing) for existing in unique_headlines):
            unique_headlines.append(headline)
    return unique_headlines 

def is_similar(headline1: str, headline2: str) -> bool:
    """Check if two headlines are similar based on 80% word overlap."""
    words1 = set(headline1.lower().split())
    words2 = set(headline2.lower().split())
    overlap = len(words1.intersection(words2))
    return overlap / max(len(words1), len(words2)) >= 0.8

def save_digest(headlines: list[str], filename: str):
    """Save the digest of headlines to a markdown file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Jarvis News Digest\n\n")
        for headline in headlines:
            f.write(f"- {headline}\n")

def collect_and_deduplicate(news_sources: list[str], filename: str):
    """Collect news from sources, deduplicate, and save to file."""
    results = asyncio.run(main(news_sources))
    # Assuming main() returns a list of headlines
    headlines = [result for result in results if "Top news:" in result]
    unique_headlines = deduplicate_headlines(headlines)
    save_digest(unique_headlines, filename)

def colorize_headline(headline: str) -> str:
    """Color code the headline based on keywords."""
    if "politics" in headline.lower():
        return f"{Fore.RED}{headline}\033[0m"  # Red for politics
    elif "sports" in headline.lower():
        return f"{Fore.GREEN}{headline}\033[0m"  # Green for sports
    elif "technology" in headline.lower():
        return f"{Fore.BLUE}{headline}\033[0m"  # Blue for technology
    else:
        return headline  # Default color


if __name__ == "__main__":
    news_sources = [
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.aljazeera.com/xml/rss/all.xml",
        "https://www.reutersagency.com/feed/?best-topics=world&post_type=best",
        "https://www.theguardian.com/world/rss"
    ]
    collect_and_deduplicate(news_sources, "digests/digest.md")




