#JSON=JavaScript Object Notation
import json #json kutuphanesi import edildi.

personString='{"name":"ali","languages":["python","ladder"]}' #json dosya formati.
result=json.loads(personString)
print(type(result))
print(result["name"])

with open("person.json","r") as f: #daha once olusturulmus json dosyasi read modunda acildi.
    data=json.load(f)  #data degiskeni icine json verileri atildi 
print(data)
print(data.items())

with open("data2.json","w") as f: #yeni json dosyasi olusturuldu ve icine veriler yazdirildi.
    json.dump(data,f)
    
personString2='{"name":"ayse","languages":["python","c++"]}' #json dosya formati.
personDictionary=json.loads(personString2)
print(personDictionary)
print(type(personDictionary))

with open("data3.json","w") as f:
    json.dump(personDictionary,f)



