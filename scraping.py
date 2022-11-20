import requests
from bs4 import BeautifulSoup
from operator import itemgetter


def get_data():
    list_of_objects = []
    emag = requests.get('https://www.emag.ro/search/laptop+dell').text
    emag_template = BeautifulSoup(emag, 'lxml')
    pages_emag = emag_template.find('span', class_='visible-xs visible-sm').text
    pages_emag = pages_emag.split()
    last_page = int(pages_emag[2])
    i = 1
    for i in range(i, last_page):
        link = requests.get(f'https://www.emag.ro/search/laptop+dell/p{i}').text
        lint_template = BeautifulSoup(link, 'lxml')
        items = lint_template.find_all('div', class_='card-v2')
        for item in items:
            if item.text != '':
                name = item.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url').text
                price = item.find('p', class_='product-new-price').text
                price = price.replace('.', '')
                price = price.replace(',', '.')
                price = price[: - 4]
                price = price.replace('de la ', '')
                element = {
                    'name': name,
                    'price': float(price),
                    'source': 'EMAG'
                }
                print(element)
                list_of_objects.append(element)

    cel = requests.get('https://www.cel.ro/cauta/laptop+dell/').text
    cel_template = BeautifulSoup(cel, 'lxml')
    pages = cel_template.find('div', class_='pageresults')
    pages = pages.text.replace('.', '')
    pages = pages.replace('>', '')
    last_page = int(pages[len(pages) - 1])
    for i in range(1, last_page):
        link = requests.get(f'https://www.cel.ro/cauta/laptop+dell/0j-{i}').text
        lint_template = BeautifulSoup(link, 'lxml')
        items = lint_template.find_all('div', class_='product_data productListing-tot')
        for item in items:
            name = item.find('h2', class_='productTitle').text
            name = name.replace('\n', '')
            price = item.find('span', class_='price').text
            element = {
                'name': name,
                'price': float(price),
                'source': 'CEL'
            }
            list_of_objects.append(element)

    flanco = requests.get('https://www.flanco.ro/catalogsearch/result/?q=laptop+dell').text
    flanco_template = BeautifulSoup(flanco, 'lxml')
    flanco_item = flanco_template.find_all('li', class_='item product product-item produs')
    for item in flanco_item:
        name = item.find('h2').text
        price = item.find_next('span', class_='price').find_next('span', class_='price').text
        price = price.replace('.', '')
        price = price.replace(',', '.')
        price = price[: - 4]
        element = {
            'name': name,
            'price': float(price),
            'source': 'FLANCO'
        }
        list_of_objects.append(element)

    new_list = sorted(list_of_objects, key=itemgetter('price'))

    return new_list


# # get_data()
#
# # cel = requests.get('https://altex.ro/cauta/?q=Laptop%20dell').text
# # cel_template = BeautifulSoup(cel, 'lxml')
# # items = cel_template.find_all('li', class_='Products-item w-1/2 sm:w-1/3 p-1 sm:p-2 border-transparent md:border-2 min-h-330px lg:min-h-400px bg-whitelg:w-1/4')
# # print(items)
# flanco = requests.get('https://www.flanco.ro/catalogsearch/result/?q=laptop+dell').text
# flanco_template = BeautifulSoup(flanco, 'lxml')
# flanco_item = flanco_template.find_all('li', class_='item product product-item produs')
# for item in flanco_item:
#     name = item.find('h2').text
#     price = item.find_next('span', class_='price').find_next('span', class_='price').text
#     price = price.replace('.', '')
#     price = price.replace(',', '.')
#     price = price[: - 4]
#     print(name)
#     print(price)
