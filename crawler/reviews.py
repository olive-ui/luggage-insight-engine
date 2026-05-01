from playwright.sync_api import sync_playwright
import pandas as pd
import time

products = pd.read_csv("data/collected/products.csv")

all_reviews = []
count = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for _, row in products.iterrows():
        brand = row["brand"]
        link = row["link"]

        if brand not in count:
            count[brand] = 0

        if count[brand] >= 51:
            continue

        try:
            asin = link.split("/dp/")[1][:10]

            for page_num in range(1, 4):
                if count[brand] >= 51:
                    break

                review_url = f"https://www.amazon.in/product-reviews/{asin}?pageNumber={page_num}"

                print("opening:", review_url)

                page.goto(review_url, timeout=60000)
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(3000)

                reviews = page.query_selector_all("span[data-hook='review-body']")

                print("found:", len(reviews))

                for r in reviews:
                    if count[brand] >= 51:
                        break

                    text = r.inner_text().strip()

                    if text:
                        all_reviews.append({
                            "brand": brand,
                            "review": text
                        })
                        count[brand] += 1

        except:
            continue

        time.sleep(2)

    browser.close()

df = pd.DataFrame(all_reviews)
df.to_csv("data/collected/reviews.csv", index=False)

print("done:", count)