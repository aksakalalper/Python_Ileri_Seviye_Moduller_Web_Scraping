import re #regular expression modulu import edildi.

str="1.cumle: Cumle yazdim. 33 yasindayim." #string cumle olusturuldu.
result=re.findall("c",str)  #cumle icinde "c" karakteri sorgulandi.
print(len(result)) 

result2=re.split(" ",str) #string cumleyi bosluk karakterlerinden itibaren boldu.
print(result2)

result3=re.sub(" ","-",str) #bosluk karakteri cizgi ile degistirildi.
print(result3)

result4=re.search("33",str) #cumle icinde "33" ifadesini aradik. true yada false dondurur.
print(result4)

result5=re.findall("[0-9]",str) #cumle icinde ifade aradi ve buldu.
print(result5)

result6=re.findall("^1",str) #cumle 1 karakteri ile basliyor mu kontrol eder.
print(result6)

result7=re.findall(".$",str) #cumle nokta karakteri ile bitiyor mu kontorl eder.
print(result7)

email = "info@yemeksepeti.com"
 
pattern = "([\w\.-]+)@([\w\.-]+)"
 
sonuc=re.findall(pattern, email)
print(sonuc)
