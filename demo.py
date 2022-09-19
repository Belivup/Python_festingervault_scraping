import requests
import csv
import uuid
from requests_html import HTMLSession
from datetime import date
s = HTMLSession()
import re

# ----------------------------------- Functions -------------------------------------------

#
# def get_products_links():
#     url = f'https://festingervault.com/wordpress-themes/'
#     links = []
#
#     r = s.get(url)
#     products = r.html.find('.fwd-m-0')
#     for item in products:
#         links.append(item.find('.fwd-m-0 a', first=True).attrs['href'])
#         return product_details
#
#     return links
#
# url = "https://festingervault.com/wordpress-themes/"
#
# def parse_products(url):
#     r = s.get(url)
#
#     versions = r.html.find('.jr-pagenav-page', first=True).attrs['title']
#     version = int(versions.split().pop(-1)) + 1
#     print(version)
#
#     product_details = {
#         'Title': version,
#     }
#     return product_details
#


def page_len():
    r = s.get('https://festingervault.com/wordpress-themes/')
    products = r.html.find('.jr-pagenav-page', first=True).attrs['title']
    page_len = int(products.split().pop(-1)) + 1

    return page_len

print(page_len())