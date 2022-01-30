# from bs4 import BeautifulSoup
html_code ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Işıl'ın Web Sitesi</title>
</head>
<body>
    <h1>Blue Akademie</h1>

    <div class="Python">
        <h2>Python GKB Course</h2>
        <ul>
            <li>Random Module</li>
            <li>Math Module</li>
            <li>Datetime Module</li>
            <li>Requests Module</li>
        </ul>
    </div>
  
    <div class="Windows">
        <h2>Windows Course</h2>
        <ul>
            <li>OS</li>
            <li>Word</li>
            <li>Excel</li>
            <li>Power Point</li>
        </ul>
    </div>

    <p>Hello Python Lovers!</p>  
    <img src="image 2.jpg"alt="">  
    <a href="http://google.com" class="sister" id="link1">Elsie</a>,
    <a href="http://yahoo.com" class="sister" id="link2">Lacie</a> and
    <a href="http://youtube.com" class="sister" id="link3">Tillie</a>

</body>
</html>
"""


# soup = BeautifulSoup(html_code, 'html.parser')
# print (soup.h1.string)
# h1 =  (soup.h1.string)
# print(h1)
# h2 =  (soup.h2.string)
# print(h2)
# h2_2 = soup.find_all("h2")
# print(h2_2[1].string)


# result= soup.find("div", {"class":"Python"})
# result2= soup.find("div", {"class":"Windows"}).find_all("li")
# for i in result2:
#     print(i.string)


# result= soup.find_all("a")
# for i in result:
#     print(i.get("href"))

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.webtekno.com/").content

soup = BeautifulSoup(r, "html.parser")
r2 = soup.find("div", {"class":"content-timeline__list"})
articleList = r2.find_all("div", {"class":"content-timeline__item"})
for i in articleList: 
    tag = i.find("h3", {"class":"content-timeline__detail__hhhtitle"})
    print (tag.string)
# print(soup)
