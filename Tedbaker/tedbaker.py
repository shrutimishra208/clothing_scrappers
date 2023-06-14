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


def listing_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-dev-shm-usage')
    service_obj = Service("/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=options)
    action_chains = ActionChains(driver)
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    listing = soup.find_all("div", class_="product-cardstyled__ProductCardContainer-g6hwh8-1 bqMxxj")
    product_list = []
    for product in listing:
        product_list.append("https://www.tedbaker.com" + product.a['href'])
    print(len(product_list))
    print(product_list)
    return product_list


def product_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-dev-shm-usage')
    service_obj = Service("/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=options)
    action_chains = ActionChains(driver)
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, "// button[ @ id = 'consent_prompt_submit']").click()
    except:
        print("no cookies to accept")
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(5)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[8]/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_name1 = soup.find("div", class_="product-detailsstyled__Header-tuq96a-1 clKlGK").find("h1").text
    product_name2 = soup.find("div", class_="product-detailsstyled__Header-tuq96a-1 clKlGK").find("h2").text
    product_name = product_name1 + " " + product_name2
    print(product_name)
    try:
        price1 = soup.find("div", class_="product-pricesstyled__Prices-sc-1hhcrv3-0")
        price = price1.find("h2", class_="product-pricesstyled__Price-sc-1hhcrv3-1 hJwDit").text
    except:
        price = None
    print(price)
    colors = []
    color = soup.find_all("div", class_="swatchstyled__SelectedColourIndicator-sc-1njw1r0-1")
    for col in color:
        colors.append(col.a['title'])
    print(colors)
    description = soup.find("div", attrs={'class': 'MuiAccordionDetails-root commonstyled__StyledAccordionDetails-sc-1of5r24-0 fwONHu'}).text
    print(description)
    fabric = soup.find("div", class_="MuiAccordionDetails-root commonstyled__StyledAccordionDetails-sc-1of5r24-0 gjhejI").find("div").text
    print(fabric)
    class_list = soup.find_all("div", class_="swiper-wrapper")
    image = class_list[2].find_all("div", class_="swiper-slide")
    print(len(image))
    images = image[0].img['srcset']
    print(images)
    data = {
        'product-url': url,
        'product_name': product_name,
        'price': price,
        'colors': colors,
        'fabric': fabric,
        'images': images,
        'description': description
    }
    driver.quit()
    return data


def main():
    url = "https://www.tedbaker.com/us/c/mens/clothing/shirts/680"
    product_links = listing_page(url)
    filename = 'in_men_tedbaker_shirts.csv'
    fieldnames = ['product-url', 'product_name', 'price', 'colors', 'fabric', 'images', 'description']
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for link in product_links:
            data = product_data(link)
            time.sleep(random.randint(1, 7))
            writer.writerow(data)


if __name__ == '__main__':
    main()