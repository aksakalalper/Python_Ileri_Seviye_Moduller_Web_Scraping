import requests #http request yapar. internet sitesine istek atar
import json

result=requests.get("https://github.com/aksakalalper/Python_Ileri_Seviye_Moduller_Web_Scraping/blob/main/info.json")
print(result)
#response[200] donerse talep basarili sonuclanir.

result=json.loads(result.text)
print(result[0])