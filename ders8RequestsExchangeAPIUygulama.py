#API(Application Programming Interface)=uygulama programlama arayuzu; iki uygulama arasinda 
#veri ve trafik akisini olusturan bir arayuzdur.

import requests #web uzerinden veri cekilecegi icin requests modulu eklendi
import json #geri donus .json formatinda olacagi icin json modulu eklendi.


apiKey="397cb65fbf243cbae2b39c22" #exhangerate-api icin olusturulan uyeligin api-key bilgisi
apiUrl="https://v6.exchangerate-api.com/v6/397cb65fbf243cbae2b39c22/latest/" #uyelige ozel api sorgu url'si

while True:
    menuChoice=input('Select a choice:\n1-Convert money\n2-Exit\n')
    if(menuChoice=="1"):
        menuText="Currency Converter"
        menuText=menuText.center(50,"*")
        print(menuText)
        givenExchange=input('From: \nUSD-EUR-TRY\n')
        givenExchange=givenExchange.upper()
        takenExchange=input('To: \nUSD-EUR-TRY\n')
        takenExchange=takenExchange.upper()
        moneyAmount=float(input("Enter amount: "))

        response=requests.get(apiUrl+givenExchange) #get metodu ile url den veri alindi
        responseJson=json.loads(response.text) #geri donus dictionary olarak atandi
        resultRate=float(responseJson["conversion_rates"][takenExchange]) #dictionary icinden veri cekildi
        result=(moneyAmount)*(resultRate) #hesaplamalar yapildi
        print(result)
    elif(menuChoice=="2"):
        break
    else:
        print('Wrong input!')
    

