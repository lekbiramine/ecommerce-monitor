from bs4 import BeautifulSoup

def parse_products(html):
    """
    Parses HTML from target search page and extracts product information.
    Returns a list of dictionaries, one per product
    """
    soup = BeautifulSoup(html, "lxml")
    product_cards = soup.select('div[data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
    products = []

    for card in product_cards:
        title_tag = card.select_one('a[data-test="product-title"]')
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        price_tag = card.select_one('span[data-test="current-price"] span')
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        comparison_tag = card.select_one('div[data-test="comparison-price"] span')
        comparison_price = comparison_tag.get_text(strip=True) if comparison_tag else None
        brand_tag = card.select_one('a[data-test*="brand"]')
        brand = brand_tag.get_text(strip=True) if brand_tag else "N/A"

        variations = []
        products.append({
            "title": title,
            "price": price,
            "comparison_price": comparison_price,
            "brand": brand,
            "variations": variations
        })
    return products