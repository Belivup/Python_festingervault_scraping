import requests
import csv
import uuid
import re
from requests_html import HTMLSession
from datetime import date
s = HTMLSession()
# from login import cookies, headers, data, HTMLSession

# s.post('https://plugintheme.net/wp-login.php', cookies=cookies, headers=headers, data=data)


# ----------------------------------- Functions -------------------------------------------


def get_products_links(page):
    url = f'https://festingervault.com/wordpress-themes/?pg={page}/'
    links = []
    r = s.get(url)
    products = r.html.find('.fwd-m-0')
    for item in products:
        links.append(item.find('.fwd-m-0 a', first=True).attrs['href'])
    return links


def parse_products(url):
    r = s.get(url)
    title = r.html.find('.elementor-heading-title', first=True) .text.strip()

    try:
        demo_link = r.html.find('.elementor-button-wrapper a', first=True).attrs['href']
    except AttributeError as err:
        demo_link = ""

    try:
        get_image = r.html.find('.dynamic-content-featuredimage-bg', first=True).attrs["style"]
        image = re.search("(?P<url>https?://[^\s]+(?:png|jpg|jpeg))", get_image).group("url")

    except AttributeError as err:
        image = "http://wpview.org/wp-content/uploads/2022/09/Image-not-found.png"

    cat = "WordPress Themes"

    try:
        f_des = r.html.find('.dce-excerpt p', first=True).text

    except AttributeError as err:
        f_des = "No Description Given, Please visit the official website for Descriptions, Thank you"



    try:
        versions = r.html.xpath('/html/body/div[2]/div/section[2]/div/div/div[2]/div/div/section[3]/div/div/div/div/div/div[2]/div/ul/li[1]/span[2]', first=True)
        version = versions.text.replace("Version ", "")

    except AttributeError as err:
        version = "Updated"

    today = date.today()
    update = today.strftime("%B %d, %Y")

    product_details = {
        'Name': title,
        'Description': f_des,
        'Status': 'publish',
        'Images': image,
        'Categories': cat,
        'Demo URL': demo_link,
        'Version': version,
        'Update': update,
        'Type': 'simple',

    }
    return product_details


def save_csv(results):
    keys = results[0].keys()

    with open('Themes.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


def page_len():
    r = s.get('https://festingervault.com/wordpress-themes/')
    products = r.html.find('.jr-pagenav-page', first=True).attrs['title']
    page_len = int(products.split().pop(-1)) + 1

    return page_len

def main():
    results = []

    for x in range(1, page_len()):
        urls = get_products_links(x)
        for url in urls:
            results.append(parse_products(url))
            print(x, parse_products(url))
        save_csv(results)

main()


#Page Len URL
#Change url
#Change Category
#Name Fies


