import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
# options.add_argument("--headless")
options.add_experimental_option('detach', True)
options.add_argument('--disable-dev-shm-usage')
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()


def base_url(url):
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/aside[1]/div[1]/button[1]/i[1]").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 15000)")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 15000)")
    time.sleep(5)
    links = driver.find_elements(By.CLASS_NAME, "product-card__body")
    product_links = []

    # saving all  the product links in a list
    for link in links:
        property1 = link.find_element(By.TAG_NAME, 'figure')
        property2 = property1.find_element(By.TAG_NAME, 'a')
        product_links.append(property2.get_property('href'))
    return product_links


def main():
    url = "https://www.nike.com/w/mens-graphic-t-shirts-5shrvznik1?sort=newest"
    product_links = base_url(url)
    print(f"total urls: {len(product_links)}")
    csv_generator(product_links)


def product_data(link):
    # products = []
    filename = "US-nike-mens-shorts.csv"
    # for url in product_links:
    driver.get(link)
    time.sleep(4)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/aside[1]/div[1]/button[1]/i[1]").click()
    # time.sleep(2)
    if driver.find_element(By.XPATH, "/html[1]/head[1]/meta[9]").get_property('content').split('/')[0] == "https:":
        product_link = driver.find_element(By.XPATH, "/html[1]/head[1]/meta[9]").get_property('content')
    else:
        product_link = driver.find_element(By.XPATH, "/html[1]/head[1]/meta[10]").get_property('content')
    time.sleep(1)
    if driver.find_element(By.XPATH, "/html[1]/head[1]/meta[10]").get_property('content').split('.')[-1] == "png":
        product_image = driver.find_element(By.XPATH, "/html[1]/head[1]/meta[10]").get_property('content')
    else:
        product_image = driver.find_element(By.XPATH, "/html[1]/head[1]/meta[11]").get_property('content')
    time.sleep(1)
    product_name = driver.find_element(By.XPATH,
                                       "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h1[1]").text
    time.sleep(1)
    product_description = driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]").text
    product_price = driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    driver.execute_script("window.scrollTo(0,700)")
    time.sleep(2)
    product_colour = driver.find_element(By.XPATH,
                                         "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/li[1]").text
    product_style = driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/li[2]").text
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/button[1]").click()
    time.sleep(2)
    about_product = driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/p[2]").text
    time.sleep(2)
    product_benefits = driver.find_elements(By.XPATH,
                                            "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]")
    product_benefits_list = []
    for item in product_benefits:
        list_item = item.text
        product_benefits_list.append(list_item)
    time.sleep(2)
    product_details = driver.find_elements(By.XPATH,
                                           "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[2]")
    product_details_list = []
    for i in product_details:
        product_details_list.append(i.text)

    product = {
        'product_name': product_name,
        'product_link': product_link,
        'product_image': product_image,
        'product_description': product_description,
        'product_price': product_price,
        'product_colour': product_colour,
        'product_style_id': product_style,
        'about_product': about_product,
        'product_benefits': product_benefits_list,
        'product_details': product_details_list
    }
    print(product)
    # products.append(product)
    time.sleep(random.randint(1, 4))
    return product


def csv_generator(product_list):
    filename = "US-nike-men-active-t-shirts.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, ['product_name', 'product_link', 'product_image', 'product_description',
                                    'product_price', 'product_colour', 'product_style_id', 'about_product',
                                    'product_benefits', 'product_details'])
        writer.writeheader()
        for product in product_list:
            data = product_data(product)
            time.sleep(random.randint(1, 6))
            writer.writerow(data)


main()
