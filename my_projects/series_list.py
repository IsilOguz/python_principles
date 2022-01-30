import imp
from webbrowser import get


import requests
from bs4 import BeautifulSoup
r = get("https://diziwatch.net/dizi-arsivi/")
soup = soup = BeautifulSoup(r, "html.parser")
r2 = soup.find("")