from playwright.sync_api import sync_playwright
import pandas as pd
import re
import time

brands = [
    "safari trolley bag",
    "skybags trolley bag",
    "vip luggage bag",
    "american tourister luggage",
    "aristocrat luggage",
    "nasher miles luggage"
]

all_products = []

with sync_playwright() as p:
    for brand in brands:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(brand)

        url = f"https://www.amazon.in/s?k={brand.replace(' ', '+')}"
        page.goto(url, timeout=60000)

        page.wait_for_timeout(5000)

        html = page.content()

        links = re.findall(r'/dp/[A-Z0-9]{10}', html)

        seen = set()
        collected = 0

        for link in links:
            if collected >= 12:
                break

            if link not in seen:
                seen.add(link)

                full_link = "https://www.amazon.in" + link

                all_products.append({
                    "brand": brand,
                    "name": link,
                    "link": full_link
                })

                collected += 1

        print("collected:", collected)

        browser.close()
        time.sleep(2)

df = pd.DataFrame(all_products)

print("total collected:", len(df))

if not df.empty:
    df.to_csv("data/collected/products.csv", index=False)
    print("saved successfully")
else:
    print("still empty")