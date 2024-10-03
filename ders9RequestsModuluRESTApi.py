#themoviedb.org 
#anahtar kelimeye gore arama
#en populer film ve vizyondaki film arama

import requests
import json

class TheMovideDb:
    def __init__(self):
        self.headers = {
                        "accept": "application/json",
                        "Authorization": " LCJ2ZXJzaW9uIjoxfQ.KyI0ZRhlvj0LpDSsgwNTo5ycAWZNT-mjmgmg0bYeBQ8"
                        }

    def getPopular(self):
       self.apiUrl="https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
       #response=requests.get(self.apiUrl,headers=self.headers)
       response=requests.get(self.apiUrl,headers=self.headers)
       return response.json()
    
runTheMovieDB=TheMovideDb()

while True:
    menuText="Select a choice"
    menuText.center(50,"*")
    print(menuText,"\n")
    userChoice=input("1-Popular movies\n2-Exit\nChoice:")
    if (userChoice=='1'):
        result=runTheMovieDB.getPopular()
        for i in result["results"]:
            print(i["title"])
        print('\n')
    elif (userChoice=='2'):
        break
    else:
        print('Wrong input!')

