

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

headers = requests.utils.default_headers()

headers.update({'User-Agent': 'My User Agent 1.0',})

URL_TEMPLATE = "https://www.gismeteo.ru/diary/4980/2023/1//"
r = requests.get(URL_TEMPLATE,  headers = headers)
print(r.status_code)


soup = bs(r.text, "html.parser")
#title = soup.find("title")
#if title:
#    print("Заголовок страницы:", title.text)
tr = soup.find("tbody").findAll("tr")
file = open("lab2.csv", "w")
for tr_item in tr:
    td = tr_item.findAll("td")
    str = ""
    for i in range(10):
        if(i == 3 or i == 4 or i == 8 or i == 9): continue;
        elif(i == 0): str += "Число" + td[i].text + ", "
        elif(i == 1): str += " День: Температура:" + td[i].text + ", "
        elif(i == 6): str += " Вечер: Температура:" + td[i].text + ", "
        elif(i == 2 or i == 7): str += "Давление:" + td[i].text + ", "
        elif(i == 5  or i == 10 ): str += "Ветер:" + td[i].text + ", "
    str += "Ветер:" + td[10].text + "\n"
    file.write(str)
file.close()
