import csv
import datetime
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_ua():
    uastrings = open('/Users/adminfashinza/fashinza/trend-scrapers/ua.txt').read().splitlines()
    return random.choice(uastrings)


def get_soup(url):
    # def get_soup(url, max_range=10, scroll_bool=0, button_bool=0)
    op = webdriver.ChromeOptions()
    op.add_argument("user-agent=" + get_ua())
    # op.add_argument("--headless")
    # op.add_argument("--no-sandbox")
    # op.add_argument('--disable-dev-shm-usage')
    # op.binary_location = "/snap/bin/chromium"
    # op.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=op)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

    # if scroll_bool == 1:
    #     y = 1000
    #     for timer in range(0, max_range):
    #         driver.execute_script("window.scrollTo(0, " + str(y) + ")")
    #         y += 1000
    #         time.sleep(1)
    #         if button_bool == 1:
    #             try:
    #                 button = driver.find_element(By.XPATH, "")
    #                 button.click()
    #             except:
    #                 continue

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup


def listing_page(url):
    op = webdriver.ChromeOptions()
    op.add_argument("user-agent=" + get_ua())
    # op.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=op)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = get_soup(url)
    # soup = get_soup(url, 200, 1)
    links = []
    pdp_divs = soup.find_all("article", class_='product-tile__plp col--6 col__xs--4 col__sm--4 col__md--3')
    print(len(pdp_divs))
    for pdp_div in pdp_divs:
        div = pdp_div.find("div").find("div", class_='product-tile-core')
        link = div.a['href']
        link = "https://www.jackjones.com"+link
        links.append(link)
    print(links)
    return links


def product_page(url):
    print(url)
    # soup = get_soup(url)
    op = webdriver.ChromeOptions()
    op.add_argument("user-agent=" + get_ua())
    op.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=op)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #title
    try:
        title = soup.find("h1", class_='product-details__title').text.strip()
    except:
        title = None
    #price
    # price_ul = soup.find("ul", class_='list-unstyled price-container')
    try:
        price_div = soup.find('div', class_='product-price__list-price')
        price = price_div.find('span').text
    except:
        price = None

    try:
        colour = soup.find('div', class_='product-details__color-options').find('div', class_='product-details__color'
                                                                                              '-annotation').text.strip()
    except:
        colour = None

    #image links
    try:
        image_links = []
        image_divs = soup.find("ul", class_='splide__list').find_all("li")
        for image_div in image_divs:
            image_links.append(image_div.find("img")['src'])
    except:
        image_links = None

    #Description
    try:
        des = soup.find("div", class_='accordion__content').find("div").find("pre").text.strip()
    except:
        des = None

    fabric = soup.find('li', class_='fabric-compostion').text.strip()
    #Details
    # details = []
    # table_div = soup.find("div", class_='accordion__content').find('div').find('div').find_all("li")
    # for table_row in table_div:
    #     details.append(table_row.text.strip())

    data = {
        'Product Link': url,
        'Product Name': title,
        'Price': price,
        'Colour': colour,
        'fabric': fabric,
        'Images': image_links,
        'Product Description': des
    }
    print(data)
    return data


def main():
    urls = ['https://www.jackjones.com/en-us/shirts?sorting=new_in&page=2']
    for url in urls:
        product_links = listing_page(url)
        # date = datetime.date.today()
        file_name = 'US_JACK&JONES_MEN_SHIRTS_NEW_ARRIVAL_21APR23.csv'
        with open(file_name, 'a') as csvfile:
            fieldnames = ['Product Link', 'Product Name', 'Price', 'Colour', 'fabric', 'Images', 'Product Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product_link in product_links:
                data = product_page(product_link)
                # try:
                #     data = product_page(product_link)
                # except:
                #     continue
                time.sleep(random.randint(1, 5))
                writer.writerow(data)


if __name__ == '__main__':
    main()
