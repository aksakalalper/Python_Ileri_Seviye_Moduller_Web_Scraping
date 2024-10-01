import requests
from bs4 import BeautifulSoup
import json

sourceURL="https://www.pttavm.com/arama/dizustu-bilgisayar?order=price_desc"
headers={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

htmlRequest=requests.get(sourceURL,headers=headers).content
soup=BeautifulSoup(htmlRequest,"html.parser")
result=soup.find("div",attrs={"class","flex flex-row flex-wrap"})
result2=soup.find_all("div",attrs={"class":"price-box flex flex-1 flex-col-reverse price-box-min-h"})

list1=[]
list2=[]

for urun in result:
    productDictKey=urun.a.get("title")
    list1.append(productDictKey)

for urun2 in result2:
    productDictValue=(urun2.text).strip()
    productDictValue=productDictValue[:-2]
    list2.append(productDictValue)

print(len(list1),len(list2))   
productDict=dict(zip(list1,list2))

with open("prices.txt","w",encoding="utf-8") as f:
    f.write(str(productDict))

with open("prices.txt","r",encoding="utf-8") as f:
    content=f.read()
    print(content)
    