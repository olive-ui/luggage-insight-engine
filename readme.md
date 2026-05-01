# Luggage Intelligence Dashboard

## Overview

This project analyzes customer reviews of major luggage brands using web scraping, data cleaning, sentiment analysis, and an interactive dashboard.

It helps identify customer satisfaction trends, common complaints, and strengths across brands.

---

## Run

```bash
pip install -r requirements.txt
py -m streamlit run ui/app.py
```

The dashboard uses the cleaned dataset from `data/curated/final.csv`.

---

## Pipeline

Data Collection → Data Cleaning → Sentiment Analysis → Insight Extraction → Dashboard Visualization

---

## Features

Scraped real product reviews
Cleaned and structured dataset
Sentiment classification (positive, neutral, negative)
Brand comparison and insights
Top complaints and positive themes
Interactive dashboard with filters

---

## Key Insights

Most brands show strong positive sentiment
Value for money is a dominant positive factor
Common issues include durability of wheels, handles, and zippers

---

## Tech Stack

Python
Pandas
Playwright
TextBlob
Streamlit
Plotly

---

## Limitations and Future Work

Limited number of products and reviews
Basic sentiment model without deep context understanding
No pricing or rating-based analysis included

Future improvements include aspect-based sentiment analysis, anomaly detection, and richer product-level insights

