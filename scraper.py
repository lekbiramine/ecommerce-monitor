from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time

def init_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def load_page(driver:WebDriver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.presence_of_element_located(
            (
            By.CSS_SELECTOR,
            'div[data-test="@web/site-top-of-funnel/ProductCardWrapper"]'
            )
        )
    )

    last_count = 0

    while True:
        driver.excecute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        cards = driver.find_elements(
            By.CSS_SELECTOR,
                'div[data-test="@web/site-top-of-funnel/ProductCardWrapper"]'
        )
        current_count = len(cards)
        if current_count == last_count:
            break

        last_count = current_count
        
    return driver.page_source
