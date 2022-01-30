"""
1-
https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

ilgili sayfadaki tüm yazıyı requests ve beautifulsoup modüllerini kullanarak çekiniz
"""

"""
2-
https://www.nytimes.com/section/politics
LİNKİNDEKİ LATEST sekmesindeki haber başlıklarını
requests ve beautifulsoup modüllerini kullanarak çekiniz


"""

# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").content

# soup = BeautifulSoup(r, "html.parser")
# r2 =  soup.find_all("p")

# for i in r2:
#     if i.string != None:
#         print(i.string)
# for i in r2:
#     print(i.string)


from typing import Counter
import requests
from bs4 import BeautifulSoup

# r = requests.get("https://www.nytimes.com/section/politics").text
# soup = BeautifulSoup(r,"html.parser")

# section = soup.find("section", {"id":"stream-panel"})
# all_titles = section.find_all("li")

# for i in all_titles:
#     if i.h2:
#         print(i.h2.text)

r = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250").content
soup = BeautifulSoup(r,"html.parser")

movieList = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=50)

for i in movieList:
    title = i.find("td",{"class":"titleColumn"}).find("a").text
    year = i.find("td",{"class":"titleColumn"}).find("span").text
    rating = i.find("td",{"class":"ratingColumn"}).find("strong").text
    print (f"Movie = {title.ljust(50)} Year = {year.ljust(20)} Rating = {rating.ljust(20)}")