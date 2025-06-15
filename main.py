# Scrape the dynamic value
#extract the price of bitcoin

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\frien\\Downloads\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier.
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://coinmarketcap.com/currencies/bitcoin/")
    return driver


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div/section/div/div[2]")
    return element.text

print(main())

