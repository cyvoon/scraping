import requests
from bs4 import BeautifulSoup

response = requests.get('http://google.com')
soup = BeautifulSoup(response.text,'lxml')
link = soup.a.get('href')
print(link)
