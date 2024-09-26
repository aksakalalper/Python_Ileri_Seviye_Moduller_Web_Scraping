import os #os modulu import edilir.
import datetime

#print(dir(os))
#os.makedirs("Python_Operatorleri/yeniklasor")
result=os.name #isletim sistemi adi
print(os.getcwd()) #etkin dizin
os.chdir('../..')#dizin degistirme
print(os.getcwd())
result2=os.listdir("c:\\")
print(result2)
print(result)
result3=os.stat("ders2OSModulu.py") #dizinde bu dosya var mi yokmu baktik
result3=datetime.datetime.fromtimestamp(result3.st_atime) #son erisilme tarihini gorduk
print(result3)

os.system("notepad.exe") #sistem uygulamasi acilir.
os.rename("newdirectory","yeniklasor")

result=os.path.abspath("ders7DigerOperatorler.py")
result=os.path.dirname()
print(result)

print(os.name)  #isletim sistemi tipi ogrenilir.
print(os.getcwd()) #mevcut dizin gosterilir.
os.chdir("c:/users/lenovo/desktop") #dizin secimi yapilir.
print(os.getcwd()) 
gecerliDizin=os.getcwd() #mevcut dizin string degere atanir.
print(os.listdir(gecerliDizin)) #mevcut dizindeki dosyalar gosterilir.
os.startfile('nordmann.txt') #dizindeki dosya acilir.
os.mkdir('yeniklasör') #dizine klasor olusturulur.
os.rename('yeniklasör','yeniklasör2') #dizindeki klasor adi degistiriir.
os.remove('deneme.txt') #dizindeki dosya silinir.
dosya=os.stat('nordmann.txt') #dizindeki dosya ozellikleri okunur.
print(dosya)
print(os.path.abspath('nordmann.txt')) #dizindeki dosyanin dosya yolu okunur.
print(os.path.exists('nordmann.txt')) #dizindeki dosyanin varligi kontrol edilir.