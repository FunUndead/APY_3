import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Java']
KEYWORDS = set(map(str.lower, KEYWORDS))
#print(KEYWORDS)

responce = requests.get('https://habr.com/ru/all/')
#print(responce.ok)
if not responce.ok:
    raise ValueError('Site not found')

text = responce.text
#print(text)
soup = BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
#print(articles)

for article in articles:
    a = article.text.strip().split()
    a = set(map(str.lower, a))
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = {h.text.strip() for h in hubs}
    hubs = set(map(str.lower, hubs))
    #print(hubs)
    #print(KEYWORDS)
    if a & KEYWORDS or hubs & KEYWORDS: # пересечение множест по тексту статьи, хабам, заголовкам
        #print(list(a & KEYWORDS))
        result_data = article.find('span', class_='tm-article-snippet__datetime-published').text  # Ищем дату интересующей статьи
        #print(result_data)
        result_tittle = article.find('a', class_='tm-article-snippet__title-link').text  # Ищем заголовок интересующей статьи
        result_link = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')  # Ищем ссылку интересующей статьи
        print(f'{result_data} - {result_tittle} - https://habr.com{result_link}')