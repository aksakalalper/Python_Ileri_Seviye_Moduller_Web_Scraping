import json

class User: #kullanici sinifi olusturuldu. veriler bu class uzerinden aktarilacak.
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository: #kullanici islemleri bu class uzerinden yapilacak.
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={} 
        #load users from .json file
        self.loadUser()

    def loadUser(self): #dosya okuma islemi yapilacak.
        with open('users.json','r') as file:
            users=json.load(file)
            print(users)

    def register(self,user:User):    
        self.users.append(user)
        self.savetoFile()
        print('kullanici olusturuldu.')

    def login(self,username,password):
        for user in self.users:
            if (user.username==username and user.password==password):
                self.isLoggedIn=True
                self.currentUser=user
                print('logged in.')
                break

    def logOut(self):
        self.isLoggedIn=False
        self.currentUser={}
        print('cikis yapildi')

    def identity(self):
        if self.isLoggedIn:
            print(f'{self.currentUser.username} ')
        else:
            print('giris yapilmadi.')

    def savetoFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__)) #liste verisini dictionary sekline cevirir.

        with open("users.json","w") as file:
            json.dump(list,file)

repository=UserRepository()

while True:
    kullaniciSecimi=input('Menu\n1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nChoice:')
    if (kullaniciSecimi=='1'):
        username=input('username: ')
        password=input('password: ')
        email=input('email: ')
        user=User(username=username,password=password,email=email)
        repository.register(user)
        print(repository.users)

    if (kullaniciSecimi=='2'):
        username=input('username: ')
        password=input('password: ')
        repository.login(username,password)

    elif (kullaniciSecimi=='3'):
        repository.logOut()
    elif (kullaniciSecimi=='4'):
        repository.loadUser()
    elif (kullaniciSecimi=='5'):
        break
    else:
        print('hatali giris yaptiniz.')
