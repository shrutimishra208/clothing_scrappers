import csv
import random
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
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
action_chains = ActionChains(driver)
driver.maximize_window()


def listing_page():
    urls = ['https://www.thereformation.com/dresses']
    product_list = []
    for url in urls:
        driver.get(url)
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/span").click()
        time.sleep(2)
        for i in range(1, 10):
            do_not = driver.find_element(By.XPATH, "//font[contains(text(),'Not just a pretty dress. Shop sustainable dresses.')]")
            action_chains.move_to_element(do_not).perform()
            time.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'html5lib')
        # listing = soup.find("div", class_="row product-grid flex-no-gutters product-grid--view-grid")
        products = soup.find_all("div", class_='product-grid__item col-6 col-md-3')
        for product in products:
            product1 = product.find("div", class_="product")
            product2 = product1.find("div", class_="product-tile product-tile--default tile--reported")
            product_list.append("https://www.thereformation.com/"+product2.a['href'])
        print(product_list)
        print(len(product_list))
        time.sleep(2)
    return product_list


def product_data(url):
    driver.get(url)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    product_name = soup.find("div", class_="pdp__title").find("h1").text.strip()
    price = soup.find("div", class_="price__sales sales").find("span", class_="price--formated").text.strip()
    colors = soup.find("div", class_="product-attribute__contents")
    try:
        colors_list = []
        colors1 = soup.find_all("button", class_="product-attribute__swatch")
        for color in colors1:
            colors_list.append(color['title'])
    except:
        colors_list = None
    # print(colors_list)
    # print(product_name, price)
    try:
        description = soup.find("div", class_="pdp__description-content").find_all("div")
        all_des = []
        for des in description:
            all_des.append(des.text.replace('\n', ''))
    except:
        all_des = None
    # print(all_des)
    try:
        details = []
        pd_details = soup.find("div", class_="pdp__accordion-content").find_all("ul")
        for d in pd_details:
            details.append(d.text.replace('\n', ''))
    except:
        details = None
    # print(details)
    material = soup.find("div", class_="pdp__accordion-content--fabric").find("div", {'data-product-component': "material"}).text.replace('\n', '')
    # print(material)
    try:
        images = []
        image = soup.find("ul", class_="product-gallery-thumbnails").find_all("li", class_="product-gallery__item product-gallery__aspect-ratio pdp__images-thumb")
        for im in image:
            images.append(im.img['src'])
    except:
        images = None
    # print(images)
    data = {
        'product_link': url,
        'product_name': product_name,
        'price': price,
        'colors': colors_list,
        'material': material,
        'images': images,
        'description': all_des,
        'product_details': details
    }
    print(data)
    return data


def csv_generator(product_list):
    filename = 'in_women_reformation_all_jeans.csv'
    fieldnames = ['product_link', 'product_name', 'price', 'colors', 'material','images', 'description', 'product_details']
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for link in product_list:
            data = product_data(link)
            time.sleep(random.randint(1, 10))
            writer.writerow(data)


def main():
    product_list = listing_page()
    csv_generator(product_list)


if __name__ == '__main__':
    main()