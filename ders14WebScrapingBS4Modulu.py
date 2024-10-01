import requests
from bs4 import BeautifulSoup

sourceURL="https://tr.wikipedia.org/wiki/Togg"
headers={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

htmlRequest=requests.get(sourceURL,headers=headers).content
soup=BeautifulSoup(htmlRequest,"html.parser")
result=soup.find("h1",{"id":"firstHeading"})
print(result)
print("**********************************************")
result2=soup.find("div",{"class":"mw-content-ltr mw-parser-output"}).text
print(result2)
print(type(result2))
with open("result.txt","w",encoding="utf-8") as f:
    f.write(result2)
 