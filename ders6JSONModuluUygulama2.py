import json
'''
personelSpecs={
    "name":"ayse",
    "age":25,
    "city":"izmir"
}

#with open("persons.json","w",encoding="utf-8") as file:
#    json.dump(personelSpecs,file)

personelSpecsUpdate={"marriage":True}

with open("persons.json","r",encoding="utf-8") as file:
    jsonTemp=json.load(file)
    jsonTemp.update(personelSpecsUpdate)

with open("persons.json","w",encoding="utf-8") as file:
    json.dump(jsonTemp,file)
    
'''

file="info.json"

while True:
    menuText="Menu"
    print(menuText.center(50,"-"))
    kullaniciGirisi=input('1-Write name and surname data\n2-Read all data\n3-Change name and surname data\n4-Add new key and value\n5-Exit\n')
    if (kullaniciGirisi=='1'):
        name=input('write name: ')
        surname=input('write surname: ')
        infoDict={
            "name":name,
            "surname":surname           
        }
        infoJSON=json.dumps(infoDict) #string olarak veriyi .json icine yazar. dumps= dict->string
        with open(file,"w") as f:
            json.dump(infoJSON,f)
            print('parameters are written.')
            #print(type(infoJSON))
    elif(kullaniciGirisi=='2'):
        with open(file,"r") as f:
            data=json.load(f) #string olarak .json verilerini yukler.
            #print(type(data))
            data2=data
            dataDict=json.loads(data2) #dictionary olarak verileri yukler.
            print(dataDict)
            #print(type(dataDict))
            print('parameters are showed.')
    elif(kullaniciGirisi=='3'):
        with open(file,"r") as f:
            data=json.load(f)
            data2=data
            dataDict=json.loads(data2)
            newName=input('enter new name: ')
            newSurname=input('enter new surname: ')
            dataDict["name"]=newName
            dataDict["surname"]=newSurname
            dataDict=json.dumps(dataDict)
        with open(file,"w") as f:
            json.dump(dataDict,f)
            print('parameters are changed.')   
    elif(kullaniciGirisi=='4'):    
        newKey=input('Enter new key: ')
        newValue=input('Enter new value: ')
        newDict={f'{newKey}':f'{newValue}'}
        print(newDict)
        with open(file,"r") as f:
            data=json.load(f)
            data2=data
            dataDict=json.loads(data2)
        dataDict.update(newDict)
        infoJSON=json.dumps(dataDict) 
        with open(file,"w") as f:
            json.dump(infoJSON,f)
            print('parameters are added.') 
    elif(kullaniciGirisi=='5'):
        break
    else:
        print('wrong input')



