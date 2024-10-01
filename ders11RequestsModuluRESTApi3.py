import requests
import json
import os
from PIL import Image

apiUrl="https://xkcd.com/368/"
response=requests.get(apiUrl)

if (response.status_code==200):
    print('Connection establieshed.')
    imageUrl="https://imgs.xkcd.com/comics/bass.png"
    imageUrl2="https://mir-s3-cdn-cf.behance.net/user/115/fed34d1504056142.66f03c1c137ff.jpg"
    response=requests.get(imageUrl2)
    imageContent=response.content
    os.chdir("c://users/lenovo/desktop")
    with open("webimage.jpg","wb") as f:
        f.write(imageContent)
    result=Image.open("c://users/lenovo/desktop/webimage.jpg")
    result.show()
    print(response.headers)

elif(response.status_code==404):
    print('Not found.')

requestUrl="https://httpbin.org/post"
payLoad={'username':'alptekin','password':'evka-5'}
response=requests.post(requestUrl,data=payLoad)
#print(response.text)
responseDict=response.json()
print(responseDict['form'])
print('********************')
requestUrl2="https://httpbin.org/get"
payLoad2={'page':2,'count':2}
response2=requests.post(requestUrl,params=payLoad)
print(response2.text)
print('********************')


