import requests #sorgu yapacagimiz icin requests modulu import edildi.
import json #geri donus .json olacagi icin json modulu import edildi.

class RickAndMorty:
    def __init__(self):
        self.apiUrl='https://rickandmortyapi.com/api/' #base url atamasi yapildi. metodlarda bunu kullanacagiz.
    def getCharacters(self):
        characterBaseCode='character' #karakter verisi icin kullanilacak anahtar kelime
        getCharactersUrl=self.apiUrl+characterBaseCode #istek yapilacak url adresi
        response=requests.get(getCharactersUrl) #requests metodu get fonksiyonu ile veri alindi.
        return response.json() #veri json formatinda cevrildi.
    def getLocations(self):
        locationBaseCode="location"
        getLocationsUrl=self.apiUrl+locationBaseCode
        response=requests.get(getLocationsUrl)
        return response.json()
    def getEpisodes(self):
        episodeBaseCode="episode"
        getEpisodesUrl=self.apiUrl+episodeBaseCode
        response=requests.get(getEpisodesUrl)
        return response.json()

rickandmorty=RickAndMorty()
while True:
    menuText="Rick and Morty"
    menuText=menuText.center(50,'*')
    print(menuText)
    userChoice=input('\nSelect a Choice\n1-See characters\n2-See locations\n3-Episodes\nChoice:\n')
    if (userChoice=='1'):
        result=rickandmorty.getCharacters()
        for i in result["results"]:
            print(i["name"],"is",i["species"])
        print('\n')
    elif (userChoice=='2'):
        result=rickandmorty.getLocations()
        for i in result["results"]:
            print(i["name"],"is",i["type"])
        print('\n')
    elif (userChoice=='3'):
        result=rickandmorty.getEpisodes()
        for i in result["results"]:
            print(i["episode"],"is",i["name"])
        print('\n')
    else:
        print('Wrong input!')

