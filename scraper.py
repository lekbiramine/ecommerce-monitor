from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

def init_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
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
    return driver.page_source
