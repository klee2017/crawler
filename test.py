import requests
from bs4 import BeautifulSoup

url = 'http://comic.naver.com/webtoon/weekday.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text)
webtoon_list = set()

day_all = soup.select_one('.list_area.daily_all')


url = 'http://comic.naver.com/webtoon/weekday.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text)

episode_list = list()


