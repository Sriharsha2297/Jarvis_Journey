# sorted() with a custom key
# Binary search concept — O(log n) — and the bisect module
# Easy LeetCode exposure: Two Sum, Valid Parentheses (just exposure, not mastery yet)
# Framing the doc uses: algorithmic thinking = systematic robot debugging.
# Resources: Andrei Neagoie's LeetCode Patterns, NeetCode roadmap.


# --- BEFORE: raw data straight off the feeds, unsorted ---
news = [
    {"source": "BBC",     "title": "Markets rally as inflation cools",        "published": "2026-07-11T08:15", "length": 31},
    {"source": "Reuters", "title": "AI chip export rules tighten",            "published": "2026-07-11T06:02", "length": 26},
    {"source": "BBC",     "title": "Storm warnings issued for coast",         "published": "2026-07-11T07:47", "length": 30},
    {"source": "Guardian","title": "New telescope maps distant galaxy",       "published": "2026-07-11T05:30", "length": 33},
    {"source": "Reuters", "title": "Central bank holds rates steady",         "published": "2026-07-11T06:02", "length": 30},
]

news = sorted(news, key=lambda x: x['published'], reverse=True )

news2 = sorted(news, key=lambda x: x['length'], reverse=True)

news3 = sorted(news, key=lambda x: x['title'].lower(), reverse=True)

news4 = sorted(news, key=lambda x: ( x['source'],x['published']))

news5 = sorted(news, key=lambda x: ( -x['length'],x['source']))

print("Sorted news by published date:")
# for item in news5:  
#     print(f"{item['published']} - {item['source']}: {item['title']} (Length: {item['length']})")    


import bisect
cycle_times = [12, 18, 25, 30, 30, 44, 51, 67]   # sorted ascending

bisect.bisect_left(cycle_times, 30)
bisect.bisect_right(cycle_times, 30)