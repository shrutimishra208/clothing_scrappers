import csv
import random
import time
import requests
from bs4 import BeautifulSoup
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/84.0.4147.105 Safari/537.36'}
main_url = "https://www.adidas.co.in/men-pants?sort=top-sellers&start="


def csv_generator(filename, product_list):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, ['Product ID', 'Product Name', 'Subtitle', 'Description', 'Standard Price',
                                    'Sale Price', 'Image Links', 'Product Details'])
        writer.writeheader()
        for product in product_list:
            writer.writerow(product)


def pagination_url(base_url, paginated_number):
    return base_url + str(paginated_number)


def main():
    paginated_number_list = [0, 48, 96]
    products = []
    filename = "product_details.csv"
    for paginated_number in paginated_number_list:
        paginated_url = pagination_url(main_url, paginated_number)
        response = requests.get(paginated_url, headers=hdr)

        soup = BeautifulSoup(response.content, 'html5lib')
        container = soup.find('div', attrs={'data-auto-id': 'product_container'})
        all_ele = container.find_all('div', {'class': 'grid-item'})

        for row in container.find_all('div', {'class': 'grid-item'}):
            product_url = row.a['href']
            product_code = product_url.split("/")[-1]  # Gives product_code.HTML
            product_code = product_code.split('.')[0]  # removing html
            product_link = f'https://www.adidas.co.in/api/products/{product_code}'
            r = requests.get(product_link, headers=hdr)
            res = r.json()
            links = res['view_list']
            images = []
            for item in links:
                image_link = item['image_url']
                images.append(image_link)
            Details = []
            for i in res['product_description'].get('usps', 'No Extra Details'):
                Details.append(i)
            # print(Details)
            product = {
                'Product ID': res['id'],
                'Product Name': res['name'].strip(),
                'Product color': res['attribute_list']['color'],
                'Product Link': res['meta_data']['canonical'].replace('//', ''),
                'Subtitle': res['product_description'].get('subtitle', "Default Subtitle"),
                'Description': res['product_description'].get('text', 'Default Text').replace('\n', ' '),
                'Standard Price': res['pricing_information']['standard_price'],
                'Sale Price': res['pricing_information'].get('sale_price', 'No Sale Price'),
                'Image Links': images,
                'Product Details': Details

            }
            products.append(product)
            time.sleep(random.randint(1, 7))

    return csv_generator(filename, products)


main()