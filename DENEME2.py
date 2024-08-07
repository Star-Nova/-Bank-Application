# Kullanıcılar
Diamond_bank_users = {
    "Gold5": {"surname": "Member", "password": "123", "tlBalance": 0, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold4": {"surname": "Member", "password": "123", "tlBalance": 1, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold3": {"surname": "Member", "password": "123", "tlBalance": 10000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold2": {"surname": "Member", "password": "123", "tlBalance": 500000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold1": {"surname": "Member", "password": "123", "tlBalance": 1000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Diamond1": {"surname": "Member", "password": "123", "tlBalance": 100000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Diamond2": {"surname": "Member", "password": "123", "tlBalance": 50000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

x_bank_users = {
    "XUser1": {"surname": "XMember", "password": "321", "tlBalance": 15000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "XUser2": {"surname": "XMember", "password": "321", "tlBalance": 200000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "XUser3": {"surname": "XMember", "password": "321", "tlBalance": 500000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "XUser4": {"surname": "XMember", "password": "321", "tlBalance": 1000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "XUser5": {"surname": "XMember", "password": "321", "tlBalance": 0, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

y_bank_users = {
    "YUser1": {"surname": "YMember", "password": "231", "tlBalance": 7500, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "YUser2": {"surname": "YMember", "password": "231", "tlBalance": 350000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "YUser3": {"surname": "YMember", "password": "231", "tlBalance": 500000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "YUser4": {"surname": "YMember", "password": "231", "tlBalance": 800000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "YUser5": {"surname": "YMember", "password": "231", "tlBalance": 0, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

rich_bank_users = {
    "RUser1": {"surname": "FMember", "password": "000", "tlBalance": 40000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "RUser2": {"surname": "FMember", "password": "000", "tlBalance": 30000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "RUser3": {"surname": "FMember", "password": "000", "tlBalance": 20000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "RUser4": {"surname": "FMember", "password": "000", "tlBalance": 10000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "RUser5": {"surname": "FMember", "password": "000", "tlBalance": 0, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

# Bankalar
banks = {
    "Diamond Bankası": {"users": Diamond_bank_users},
    "X Bankası": {"users": x_bank_users},
    "Y Bankası": {"users": y_bank_users},
    "Rich Bankası": {"users": rich_bank_users}
}

# Döviz, altın ve coin fiyatları
exchange_rates = {
    "Dolar": 33,
    "Euro": 35,
    "Japonyeni": 5,
    "Sterlin": 40,
    "KuveytDinarı": 100,
    "ÇinYuanı": 6,
    "GramAltın": 2500,
    "ÇeyrekAltın": 4000,
    "YarımAltın": 8000,
    "TamAltın": 16000,
    "Bitcoin": 2300000,
    "Ethereum": 122000,
    "Tether": 32,
    "BNB": 23000
}

# Banka hakkında bilgi
bank_info = "Diamond Bankası 1999 yılında kuruldu. Her zaman güvenli sistemimizle paranızı muhafaza etmekteyiz. Bankamızın kurucusu Fernando'dur. 25 yıldır Türkiye'de milyonların paralarını güvenli bir şekilde muhafaza ettik. Bankamızı tercih ettiğiniz için teşekkür ederiz."

# Engellenen kullanıcı listesi
blocked_users = {
    "Diamond Bankası": ["Gold5"],
    "X Bankası": ["XUser5"],
    "Y Bankası": ["YUser5"],
    "Rich Bankası": ["RUser5"]
}

# Kullanıcı girişi veya hesap açma menüsü
def main_menu():
    print("\n1. Giriş Yap")
    print("2. Hesap Aç")
    print("3. Çıkış")
    choice = int(input("Bir seçenek girin (1, 2 veya 3): "))
    return choice

# Yeni kullanıcı oluşturma
def create_account():
    username = input("Kullanıcı adınızı girin: ")
    surname = input("Soyadınızı girin: ")
    password = input("Şifrenizi belirleyin: ")
    print("Bankalar: 1. Diamond Bankası, 2. X Bankası, 3. Y Bankası, 4. Rich Bankası")
    bank_choice = int(input("Hangi bankada hesap açmak istiyorsunuz? (1, 2, 3 veya 4): "))

    if bank_choice == 1:
        bank_name = "Diamond Bankası"
    elif bank_choice == 2:
        bank_name = "X Bankası"
    elif bank_choice == 3:
        bank_name = "Y Bankası"
    elif bank_choice == 4:
        bank_name = "Rich Bankası"
    else:
        print("Geçersiz seçim! Hesap açma işlemi iptal edildi.")
        return None, None

    if username in banks[bank_name]["users"]:
        print("Bu kullanıcı adı zaten mevcut! Lütfen başka bir kullanıcı adı seçin.")
        return None, None

    # Yeni kullanıcıyı bankaya ekleyin
    banks[bank_name]["users"][username] = {
        "surname": surname,
        "password": password,
        "tlBalance": 0,
        "coinAmount": 0,
        "valuableAmount": 0,
        "transactions": []
    }

    print(f"{username} kullanıcısı {bank_name} bankasında başarıyla oluşturuldu.")
    return username, bank_name

# Kullanıcı girişi
def login():
    print("Lütfen giriş yapın.")
    for _ in range(5):
        username = input("Kullanıcı adınızı giriniz: ")
        surname = input("Soyadınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        bank_name = input("Hangi bankaya aitsiniz? (Diamond Bankası / X Bankası / Y Bankası / Rich Bankası): ")

        if bank_name in banks and username in banks[bank_name]["users"]:
            user = banks[bank_name]["users"][username]
            
            # Engelleme kontrolü
            if username in blocked_users.get(bank_name, []):
                print("Sisteme girişiniz engellenmiştir!")
                continue
            
            if user["surname"] == surname and user["password"] == password:
                print("Sisteme başarıyla giriş yaptınız!")
                return username, bank_name
            else:
                print("Şifre veya soyadı yanlış!")
        else:
            print("Kullanıcı bulunamadı!")
    return None, None

# Hesap bilgilerini görüntüleme
def show_account_details(username, bank_name):
    user = banks[bank_name]["users"][username]
    print(f"\nHesap Bilgileri: \nKullanıcı Adı: {username}\nSoyadı: {user['surname']}\nTL Bakiye: {user['tlBalance']} TL\nKripto Bakiye: {user['coinAmount']} coin\nDeğerli Eşya Miktarı: {user['valuableAmount']}\n")

# Menü
def menu():
    while True:
        choice = main_menu()
        if choice == 1:
            username, bank_name = login()
            if username and bank_name:
                show_account_details(username, bank_name)
        elif choice == 2:
            create_account()
        elif choice == 3:
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

# Programı başlat
menu()
