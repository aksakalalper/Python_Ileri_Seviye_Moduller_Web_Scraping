import datetime

now=datetime.datetime.now() #suan saat kac 
print(now)
print(now.day)

now2=datetime.datetime.ctime(now) #takvim formatinda verdi.
print(now2)
sonuc=datetime.datetime.strftime(now,'%y') #tarih saat ogesinin spesifik parametresini string olarak dondurur.
print(sonuc)

t='26 September 2024 hour 14:53:30'
dt=datetime.datetime.strptime(t,'%d %B %Y hour %H:%M:%S') #string tarih verisini tarih zaman formatina cevirir.
print(dt)

dogumgunu=datetime.datetime(1995,10,18) #tarih degiskeni olusturuldu.
print(dogumgunu)

t='26 october 2022'
yasBilgisiDT=datetime.datetime.strptime(t,'%d %B %Y')
yasBilgisiDT=yasBilgisiDT+datetime.timedelta(days=150)
islem=input('isleme baslamak icin 1 e bas:\n')
if(islem=='1'):
 fark=now-yasBilgisiDT
 print(fark)





