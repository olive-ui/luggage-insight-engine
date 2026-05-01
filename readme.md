# Luggage Intelligence Dashboard

## Overview

This project explores customer reviews of popular luggage brands using web scraping, basic NLP, and visualization. The aim was to understand how customers actually feel about different brands and identify common strengths and issues from their feedback.

## Features

Collected real product and review data using web scraping
Cleaned and structured raw text data
Performed sentiment analysis with positive, negative, and neutral classification
Built an interactive dashboard to visualize insights
Extracted common complaint keywords from negative reviews

## Tech Stack

Python, Pandas, Playwright, TextBlob, Streamlit, Plotly

## Key Insights

Most brands show a high level of positive sentiment
Common issues include wheels, handles, and zipper durability
Value for money appears frequently in positive feedback
Some brands are more consistent in customer satisfaction than others

## How to Run

```bash
py -m streamlit run ui/app.py
```

## Notes

This project focuses on building a complete pipeline from data collection to insight generation. It highlights working with real world data and presenting meaningful patterns in a simple and interactive way.
