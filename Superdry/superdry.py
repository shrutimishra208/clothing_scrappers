import csv
import random
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_experimental_option('detach', True)
options.add_argument('--disable-dev-shm-usage')
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()


def listing_page(url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    listing = soup.find("div", attrs={'class': 'pdp-search-results-product-list'})
    products = listing.find_all("div", attrs={"class": "content"})
    products_list = []
    for product in products:
        product1 = product.find("div", attrs={'class': 'productListingLazyImage product-img'})
        # products2 = product1.find("div", attrs={'class': 'image image-swap-effect'})
        products_list.append("https://www.superdry.com"+product1.a['href'])
    print(len(products))
    print(products_list)
    return products_list


def product_data(url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    product_name = soup.find("div", attrs={'class': 'col-sm-6 col-md-5 right-hand-column'}).find("h1").text
    # print(product_name)
    price = soup.find('div', class_='col-sm-6 col-md-5 right-hand-column').find("h2").text
    # print(price)
    sizes = soup.find('div', class_='form-group required').find("div", attrs={'di': 'input-option1799482'})
    sizes1 = soup.find_all("div", attrs={'class': 'radio radio-type-button2'})
    size_list = []
    for size in sizes1:
        size_list.append(size.find('label').text)
    # print(size_list)
    images = []
    image = soup.find_all('div', class_='image-additional')
    for im in image:
        images.append(im.a['href'])
    # print(images)
    try:
        additional_info = soup.find('table', class_='table table-bordered').find('tbody').find_all('td')
    except:
        additional_info = None
    # print(additional_info[1].text)
    try:
        material = soup.find('table', class_='specificationTable').find_all('td')[1].text
    except:
        material = None

    data = {
        'product link': url,
        'product name': product_name,
        'price': price,
        'material': material,
        'size information': size_list,
        'images': images,
        'additional_info': additional_info
    }
    return data


def main():
    urls = ['https://www.superdry.com/us/mens/gym?scrollYPos=0&types=Sports%20T-Shirt%2CSports%20Top']
    for url in urls:
        product_links = listing_page(url)
        filename = 'US_SUPERDRY_MEN_ACTIVE_TSHIRTS.CSV'
        fieldnames = ['product link', 'product name', 'price', 'material', 'size information', 'images', 'additional_info']
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for link in product_links:
                data = product_data(link)
                time.sleep(random.randint(1, 10))
                writer.writerow(data)


if __name__ == '__main__':
    main()