import requests
from bs4 import BeautifulSoup
import re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
albums=[]
file_url = r'C:\Users\483\Desktop\Русик файлы\russian albums'
url='https://music.yandex.ru/genre/%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D0%BE%D0%BA/albums/popular'
iter=-1
count = 0
html= requests.get(url)
html2=''
bad=['Аквариум','Машина времени','Андрей Макаревич','ДДТ','Земфира','Би-2 ']

soup = BeautifulSoup(html.text,'lxml')
for aaa in range(0,300):
    if aaa!=0:
        html2=url+f'?page={aaa}'
        html2=requests.get(html2)
        soup= BeautifulSoup(html2.text,'lxml')
    year = soup.find_all(class_='album__year deco-typo-secondary typo-add')
    if year=='[]':
        break
    else:
        title = soup.find_all(class_='d-link deco-link album__caption')
        group = soup.find_all(class_='album__artist deco-typo-secondary typo-add')
        for i in year:
            count += 1
            iter += 1
            str = ''
            str = i.text.replace(' ', '')
            if str[:4].isalpha() or str[:4]=='' or group[iter].text in bad or has_cyrillic(group[iter].text)==False:
                continue
            if int(str[:4]) >= int('1990') and int(str[:4]) <= int('1990'):
            #if group[iter].text in good:
                endname = f'{count} место: {str[:4]} {group[iter].text} - {title[iter].text}'
                print(endname)
                albums.append(endname)
                my_file = open(f'{file_url}\_russian 1990.txt', 'a', encoding='utf-8')
                my_file.write(endname + '\n')
                my_file.close()
            else:
                print(f'страница {aaa} {count} место: {str[:4]} {group[iter].text} - {title[iter].text}')

        iter = -1





