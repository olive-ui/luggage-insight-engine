import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/refined/cleaned.csv")

def sentiment(text):
    s = TextBlob(text).sentiment.polarity
    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["review_text"].apply(sentiment)

df.to_csv("data/curated/final.csv", index=False)

print("sentiment done")