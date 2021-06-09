import csv

import requests
from bs4 import BeautifulSoup

url = 'https://glycemicindex.com/gi-search/'
page = requests.get(url=url)

soup = BeautifulSoup(page.text, 'html5lib')

data = soup.find_all(name='table', id='tablepress-1')
tabs = data[0]
f = open('gi2.csv', 'w', encoding='utf-8')
for tr in tabs.find_all('tr'):
    for td in tr.find_all('td'):
        if td.text != '':
            f.write(td.text)
        else:
            f.write('')
        f.write('#')
    f.write('\r\n')
