import requests
from bs4 import BeautifulSoup as BS
import time
import random

n1 = input('От: ')
n2 = input('До: ')
filename = n1 + '-' + n2 + '_rusprofile.txt'
interval = int(input('Максимальный интервал: '))
interval = random.randint(0, interval)

for page in range(int(n1), int(n2)):
    page += 1
    time.sleep(interval)
    url = 'https://www.rusprofile.ru/codes/561010/' + str(page)
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    name = soup.select('.company-item-info')

    for i in range(0, len(name), 3):
        if name[i].dd.text.isdigit():
            i += 1
        else:
            with open(filename, 'a') as file:
                file.write(name[i].dd.text + '\n')

