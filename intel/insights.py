import pandas as pd
from collections import Counter

df = pd.read_csv("data/curated/final.csv")

negative = df[df["sentiment"] == "negative"]["review_text"]

words = []

for review in negative:
    for w in review.lower().split():
        if len(w) > 3:
            words.append(w)

common = Counter(words).most_common(10)

print("Top complaints:")
for w, c in common:
    print(w, c)