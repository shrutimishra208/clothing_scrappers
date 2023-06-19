import csv
import random
import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_ua():
    # uastrings = open('/home/vaibhavbaswal/MLE/ua.txt').read().splitlines()
    return random.choice(open(r"/Users/adminfashinza/fashinza/trend-scrapers/ua_windows.txt").readlines())


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=" + get_ua())
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-dev-shm-usage')
    service_obj = Service("/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=options)
    action_chains = ActionChains(driver)
    driver.maximize_window()
    return driver


def listing_page(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    # print(soup)
    time.sleep(2)
    products = soup.find_all("article", class_="searchProduct-wrapper")
    print(len(products))
    product_list = []
    for product in products:
        product_list.append(product.a['href'])
    print(product_list)
    driver.quit()
    time.sleep(5)
    return product_list


def product_data(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    try:
        product_name = soup.find("h1", class_="productName").text
    except:
        product_name = None

    try:
        price = []
        price1 = soup.find_all("div", class_="priceUpdater")
        price2 = price1[1].find("div", class_="hidden").text.strip().replace('\n' and ' ', '')
        price.append(price2)
    except:
        price = None
    print(price)

    try:
        color = soup.find("div", class_="inner color-thumbnail-wrapper").img['title']
    except:
        color = None
    print(color)
    print(product_name)

    try:
        description = soup.find("div", class_="attributesUpdater editorialdescription").text.strip()
    except:
        description = None
    print(description)

    try:
        details = []
        pd_details = soup.find("div", class_="attributesUpdater itemdescription").text.strip()
        details.append(pd_details)
    except:
        details = None
    print(details)

    try:
        image = soup.find("div", class_="swiper-slide swiper-slide-1 has-zoom swiper-slide-active").picture.img['src']
    except:
        image = None
    print(image)
    data = {
        'product_name': product_name,
        'product_url': url,
        'price': price,
        'color': color,
        'image': image,
        'description': description,
        'product_details': details
    }
    driver.quit()
    print(data)
    return data


def main():
    urls = ["https://www.chloe.com/in/see-by-chloe/shop-online/women/see-by-chloe-dresses"]
    for url in urls:
        product_links = listing_page(url)
        # print(len(product_links))
        filename = "us_chloe_women_dresses.csv"
        fieldnames = ['product_url', 'product_name', 'price', 'color', 'image', 'description', 'product_details']
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for link in product_links:
                data = product_data(link)
                time.sleep(random.randint(1, 10))
                writer.writerow(data)


if __name__ == '__main__':
    main()
