import sys
from bs4 import BeautifulSoup
import requests
url = sys.argv[1:]
re=requests.get('https://'+url[0]);
data =re.text
soup =BeautifulSoup(data)
for link in soup.find_all('a'):

    print(link.get('href'))
