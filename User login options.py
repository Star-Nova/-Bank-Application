import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = None
        self.loadUsers()

    def loadUsers(self):
        """Load users from 'user_information.json' file if it exists."""
        if os.path.exists('user_information.json'):
            with open('user_information.json', 'r') as file:
                users_data = json.load(file)
                for user_data in users_data:
                    user = User(user_data['username'], user_data['password'], user_data['email'])
                    self.users.append(user)

    def saveUsers(self):
        """Save the current users list to 'user_information.json' file."""
        with open('user_information.json', 'w') as file:
            users_data = [{'username': user.username, 'password': user.password, 'email': user.email} for user in self.users]
            json.dump(users_data, file, indent=4)

    def register(self, user: User):
        """Register a new user if the username is not already taken."""
        if any(u.username == user.username for u in self.users):
            print('Bu kullanıcı adı zaten mevcut.')
        else:
            self.users.append(user)
            self.saveUsers()
            self.saveUserInfo(user)
            print('Kullanıcı oluşturuldu')

    def saveUserInfo(self, user: User):
        """Save user info to 'user_information.json' file."""
        user_info = {'username': user.username, 'password': user.password, 'email': user.email}
        if os.path.exists('user_information.json'):
            with open('user_information.json', 'r') as file:
                users_info = json.load(file)
        else:
            users_info = []
        
        users_info.append(user_info)
        
        with open('user_information.json', 'w') as file:
            json.dump(users_info, file, indent=4)
        print('Kullanıcı bilgileri "user_information.json" dosyasına kaydedildi.')

    def login(self, username, password):
        """Log in a user by username and password."""
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Giriş başarılı')
                return
        print('Yanlış kullanıcı adı veya şifre')

    def logout(self):
        """Log out the current user if logged in."""
        if self.isLoggedIn:
            self.isLoggedIn = False
            self.currentUser = None
            print('Çıkış yapıldı')
        else:
            print('Zaten giriş yapılmamış')

    def identity(self):
        """Display the current logged-in user's identity."""
        if self.isLoggedIn:
            print(f'Giriş yapılan kullanıcı: {self.currentUser.username}')
        else:
            print('Giriş yapılmamış')

repository = UserRepository()

while True:
    print('Menü'.center(50, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim == '5':
        break
    elif secim == '1':
        username = input('Kullanıcı adı: ')
        password = input('Şifre: ')
        email = input('Email: ')
        user = User(username=username, password=password, email=email)
        repository.register(user)
    elif secim == '2':
        username = input('Kullanıcı adı: ')
        password = input('Şifre: ')
        repository.login(username, password)
    elif secim == '3':
        repository.logout()
    elif secim == '4':
        repository.identity()
    else:
        print('Yanlış seçim')
