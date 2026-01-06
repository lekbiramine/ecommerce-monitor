from scraper import init_driver, load_page
from parser import parse_products
from config import SEARCH_URL, HISTORY_FILE, PRODUCT_LIST_FILE
from storage.storage import save_current_products, append_price_history

def main():
    driver = init_driver()
    try:
        html = load_page(driver, SEARCH_URL)
        products = parse_products(html)
        save_current_products(products, PRODUCT_LIST_FILE)
        append_price_history(products, HISTORY_FILE)
    finally:
        # driver.quit()
        input("Press Enter to close the browser...")
        driver.quit()
if __name__ == "__main__":
    main()
