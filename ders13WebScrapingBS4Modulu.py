import requests
from bs4 import BeautifulSoup

sourceURL="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

#header'a tarayici ozelliklerini kopyalayarak sanki tarayicidan talep yapmisiz gibi davrandi.
header={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

htmlResult=requests.get(sourceURL,headers=header).content #403 hatasi=talep tarayici tarafindan engelleniyor.
soup=BeautifulSoup(htmlResult,"html.parser") #html parser eklendi
result=soup.find("div",{"class":"ipc-page-grid"}).find_all("li")

for item in result:
    movieName=item.find("h3",{"class":"ipc-title__text"}).text
    print(movieName)


