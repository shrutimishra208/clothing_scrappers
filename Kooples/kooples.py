import csv
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


def get_ua():
    uastrings = open('/Users/adminfashinza/fashinza/trend-scrapers/ua.txt').read().splitlines()
    return random.choice(uastrings)


def product_page(link):
    print(link)
    op = webdriver.ChromeOptions()
    op.add_argument("user-agent=" + get_ua())
    op.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=op)
    driver.get(link)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    #title
    title = soup.find("h1").text

    #price
    price = soup.find("span", class_='sales skp-sales').find("span").text

    #image links
    image_links = []
    image_lis = soup.find_all("div", class_='slick-item')
    for li in image_lis:
        try:
            image_links.append(li.find("img")['src'])
        except TypeError:
            continue

    #colors
    '//div[contains(@data-attr,"color")]//div[contains(@class,"attribute")]'
    colors = []
    colors_div = soup.find("div", attrs={'data-attr':'color'}).find("div", class_='attribute').find_all("a")
    for atag in colors_div:
        colors.append(atag['aria-label'][14:])

    #description
    des_list = []
    try:
        des_div = soup.find("div", class_='accordion-content content first-content').find("div").find("ul").find_all("li")
    except AttributeError:
        des_div = soup.find("div", class_='accordion-content content first-content').find("div").find_all("li")
    for li in des_div:
        des_list.append(li.text.strip())

    #fabric
    fabric = []
    fabric_divs = soup.find("div", class_='materials-care-origin').find_all("div")
    for div in fabric_divs:
        if ":" in div.text:
            fabric.append(div.text.strip())

    data = {'Product Link': link,
            'Product name': title,
            'Price': price.strip(),
            'Images': image_links,
            'Product Description': des_list,
            'Color': colors,
            'Fabric': fabric}
    print(data)
    return data


def listing_page(url):
    op = webdriver.ChromeOptions()
    op.add_argument("user-agent=" + get_ua())
    op.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=op)
    driver.get(url)
    time.sleep(1)

    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        time.sleep(2)
        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'VIEW MORE')]"):
                driver.find_element(By.XPATH, "//button[contains(.,'VIEW MORE')]").click()
        except :
            continue

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    base_url = 'https://www.thekooples.com'
    urls = []
    links = soup.find_all("a", class_='link-url')
    for link in links:
        urls.append(base_url + link['href'])
        print(len(urls))
    return urls


def main():
    urls = ['https://www.thekooples.com/us/en_US/women/ready-to-wear/dresses-and-jumpsuits']
    # urls = ['https://www.thekooples.com/int/en/women/ready-to-wear/dresses-and-jumpsuits/short-black-dress-FROB25146KBLA01.html']
    for url in urls:
        products = listing_page(url)
        print(len(products))
        file_name = 'us-kooples-women_dresses.csv'
        with open(file_name, 'a') as csvfile:
            fieldnames = ['Product Link', 'Product name', 'Color',
                          'Price', 'Images', 'Fabric', 'Product Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for link in products:
                data = product_page(link)
                time.sleep(random.randint(1, 5))
                writer.writerow(data)
        # print(listing_page(url))
        # product_page(url)


if __name__ == '__main__':
    main()
