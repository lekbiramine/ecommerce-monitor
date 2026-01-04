from scraper import init_driver, load_page
from parser import parse_products
from config import SEARCH_URL
from storage.storage import save_current_products

def main():
    driver = init_driver()
    try:
        html = load_page(driver, SEARCH_URL)
        products = parse_products(html)
        print("Products:")
        print(products)
        print(f"Number of products: {len(products)}")
        save_current_products(products, "data/products.xlsx")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
