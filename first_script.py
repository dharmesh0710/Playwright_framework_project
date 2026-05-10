from playwright.sync_api import sync_playwright
import time

def main():
    # Start the Playwright engine
    with sync_playwright() as p:
        # Launch Chromium. headless=False means we can visibly see the browser open.
        browser = p.chromium.launch(headless=False)
        
        # Open a new browser tab/page
        page = browser.new_page()
        
        # Navigate to our target E-commerce site
        print("Navigating to the website...")
        page.goto("https://practicesoftwaretesting.com/")
        
        # Grab the page title and print it
        page_title = page.title()
        print(f"Success! The page title is: '{page_title}'")
        
        # Pause for 3 seconds just so you can see it before it closes
        time.sleep(3)
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()