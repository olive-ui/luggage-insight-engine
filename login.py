from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="user_data",
        headless=False
    )
    page = context.new_page()

    page.goto("https://www.amazon.in")
    print("Login manually in the opened browser, then close it.")

    input("Press Enter after logging in...")

    context.close()