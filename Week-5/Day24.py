# sets — unique collections, fast membership
# deque from collections
# defaultdict — automatic defaults
# Counter — count occurrences
# namedtuple
# Practice: word frequency counter using Counter

import collections
from collections import Counter


D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
A = ['hall', 'house', 'home', 'hat', 'horse']
D = Counter(D)  
A = Counter(A)

print(D)  # Output: Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1})
print(A)  # Output: Counter({'hall': 1, 'house': 1, 'home': 1, 'hat': 1, 'horse': 1})