# Banka Uygulaması

# Kullanıcılar
PYT_bank_users = {
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
    "PYT Bankası": {"users": PYT_bank_users},
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
bank_info = "PYT BANKASI 1999 yılında kuruldu. Her zaman güvenli sistemimizle paranızı muhafaza etmekteyiz. Bankamızın kurucusu Fernando'dur. 25 yıldır Türkiye'de milyonların paralarını güvenli bir şekilde muhafaza ettik. Bankamızı tercih ettiğiniz için teşekkür ederiz."

# Engellenen kullanıcı listesi
blocked_users = {
    "PYT Bankası": ["Gold5"],
    "X Bankası": ["XUser5"],
    "Y Bankası": ["YUser5"],
    "Rich Bankası": ["RUser5"]
}

# Kullanıcı girişi
def login():
    print("Lütfen giriş yapın.")
    for _ in range(5):
        username = input("Kullanıcı adınızı giriniz: ")
        surname = input("Soyadınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        bank_name = input("Hangi bankaya aitsiniz? (PYT Bankası / X Bankası / Y Bankası / Rich Bankası): ")

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
            print("Kullanıcı adı veya banka bilgisi yanlış!")

    print("Giriş hakkınız doldu. Sistem kapatılıyor.")
    return None, None

# ATM menüsü
def atm_menu(username, bank_name):
    print("\n1. Profil")
    print("2. Bakiye sorgula")
    print("3. Para yatır")
    print("4. Para çek")
    print("5. Hesap özeti")
    print("6. Banka hakkında bilgi al")
    print("7. Havale")
    print("8. EFT")
    print("9. Altın alımı")
    print("10. Coin alımı")
    print("11. Döviz alımı")
    print("12. Altın satımı")
    print("13. Coin satımı")
    print("14. Döviz satımı")
    print("15. Çıkış yap")
    if username in ["Diamond1", "Diamond2"]:
        print("16. Kullanıcıları görüntüle")

# Kullanıcı profili gösterme
def show_profile(username, bank_name):
    user = banks[bank_name]["users"][username]
    print("Profil Bilgileri:")
    print(f"Kullanıcı Adı: {username}")
    print(f"Soyadı: {user['surname']}")
    print(f"Bakiye: {user['tlBalance']} TL")
    print(f"Altın Miktarı: {user['valuableAmount']}")
    print(f"Coin Miktarı: {user['coinAmount']}")
    print("İşlem Geçmişi:")
    for transaction in user['transactions']:
        print(f"- {transaction}")

# Kullanıcıları görüntüleme
def show_users(bank_name):
    for user, info in banks[bank_name]["users"].items():
        print(f"Kullanıcı Adı: {user}, Soyadı: {info['surname']}, Bakiye: {info['tlBalance']} TL")

# Para yatırma
def deposit(username, bank_name):
    amount = int(input("Yatırılacak tutarı girin: "))
    banks[bank_name]["users"][username]['tlBalance'] += amount
    banks[bank_name]["users"][username]['transactions'].append(f"{amount} TL yatırıldı.")
    print(f"{amount} TL başarıyla yatırıldı.")

# Para çekme
def withdraw(username, bank_name):
    amount = int(input("Çekilecek tutarı girin: "))
    if amount <= banks[bank_name]["users"][username]['tlBalance']:
        banks[bank_name]["users"][username]['tlBalance'] -= amount
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} TL çekildi.")
        print(f"{amount} TL başarıyla çekildi.")
    else:
        print("Hesabınızda yeterli bakiye yok.")

# Hesap özeti gösterme
def show_account_summary(username, bank_name):
    user = banks[bank_name]["users"][username]
    print("Hesap Özeti:")
    for transaction in user['transactions']:
        print(f"- {transaction}")

# Havale yapma
def transfer(username, bank_name):
    receiver = input("Para göndermek istediğiniz kişinin kullanıcı adını girin: ")

    # Engelleme kontrolü
    if receiver in blocked_users.get(bank_name, []):
        print(f"{receiver} kullanıcısı engellenmiştir. Havale işlemi yapılamaz.")
        return

    amount = int(input("Göndermek istediğiniz miktarı girin: "))
    if receiver in banks[bank_name]["users"]:
        if amount <= banks[bank_name]["users"][username]['tlBalance']:
            banks[bank_name]["users"][username]['tlBalance'] -= amount
            banks[bank_name]["users"][receiver]['tlBalance'] += amount
            banks[bank_name]["users"][username]['transactions'].append(f"{amount} TL {receiver} hesabına havale yapıldı.")
            banks[bank_name]["users"][receiver]['transactions'].append(f"{amount} TL {username} hesabından havale geldi.")
            print(f"{amount} TL {receiver} hesabına başarıyla gönderildi.")
        else:
            print("Yetersiz bakiye!")
    else:
        print("Alıcı kullanıcı bulunamadı!")

# EFT yapma
def eft(username, bank_name):
    other_bank = input("EFT yapacağınız bankayı girin: ")
    receiver = input("EFT yapacağınız kişinin kullanıcı adını girin: ")

    # Engelleme kontrolü
    if receiver in blocked_users.get(other_bank, []):
        print(f"{receiver} kullanıcısı {other_bank} bankasında engellenmiştir. EFT işlemi yapılamaz.")
        return

    amount = int(input("EFT yapmak istediğiniz miktarı girin: "))
    if other_bank in banks and receiver in banks[other_bank]["users"]:
        if amount <= banks[bank_name]["users"][username]['tlBalance']:
            banks[bank_name]["users"][username]['tlBalance'] -= amount
            banks[other_bank]["users"][receiver]['tlBalance'] += amount
            banks[bank_name]["users"][username]['transactions'].append(f"{amount} TL {receiver} hesabına EFT yapıldı.")
            banks[other_bank]["users"][receiver]['transactions'].append(f"{amount} TL {username} hesabından EFT geldi.")
            print(f"{amount} TL {receiver} hesabına başarıyla EFT yapıldı.")
        else:
            print("Yetersiz bakiye!")
    else:
        print("Geçersiz banka veya kullanıcı adı!")

# Altın alımı
def buy_gold(username, bank_name):
    print(f"Gram Altın: {exchange_rates['GramAltın']} TL")
    print(f"Çeyrek Altın: {exchange_rates['ÇeyrekAltın']} TL")
    print(f"Yarım Altın: {exchange_rates['YarımAltın']} TL")
    print(f"Tam Altın: {exchange_rates['TamAltın']} TL")

    gold_type = input("Almak istediğiniz altını seçin (Gram/Çeyrek/Yarım/Tam): ")
    amount = int(input("Kaç adet almak istiyorsunuz? "))
    total_price = amount * exchange_rates[f'{gold_type}Altın']

    if total_price <= banks[bank_name]["users"][username]['tlBalance']:
        banks[bank_name]["users"][username]['tlBalance'] -= total_price
        banks[bank_name]["users"][username]['valuableAmount'] += total_price
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} adet {gold_type} altın satın alındı.")
        print(f"{amount} adet {gold_type} altın başarıyla satın alındı.")
    else:
        print("Yetersiz bakiye!")

# Coin alımı
def buy_coin(username, bank_name):
    print(f"Bitcoin: {exchange_rates['Bitcoin']} TL")
    print(f"Ethereum: {exchange_rates['Ethereum']} TL")
    print(f"Tether: {exchange_rates['Tether']} TL")
    print(f"BNB: {exchange_rates['BNB']} TL")

    coin_type = input("Almak istediğiniz coini seçin (Bitcoin/Ethereum/Tether/BNB): ")
    amount = int(input("Kaç adet almak istiyorsunuz? "))
    total_price = amount * exchange_rates[coin_type]

    if total_price <= banks[bank_name]["users"][username]['tlBalance']:
        banks[bank_name]["users"][username]['tlBalance'] -= total_price
        banks[bank_name]["users"][username]['coinAmount'] += amount
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} adet {coin_type} satın alındı.")
        print(f"{amount} adet {coin_type} başarıyla satın alındı.")
    else:
        print("Yetersiz bakiye!")

# Döviz alımı
def buy_currency(username, bank_name):
    print(f"Dolar: {exchange_rates['Dolar']} TL")
    print(f"Euro: {exchange_rates['Euro']} TL")
    print(f"Japonyeni: {exchange_rates['Japonyeni']} TL")
    print(f"Sterlin: {exchange_rates['Sterlin']} TL")
    print(f"Kuveyt Dinarı: {exchange_rates['KuveytDinarı']} TL")
    print(f"Çin Yuanı: {exchange_rates['ÇinYuanı']} TL")

    currency_type = input("Almak istediğiniz dövizi seçin (Dolar/Euro/Japonyeni/Sterlin/KuveytDinarı/ÇinYuanı): ")
    amount = int(input("Kaç adet almak istiyorsunuz? "))
    total_price = amount * exchange_rates[currency_type]

    if total_price <= banks[bank_name]["users"][username]['tlBalance']:
        banks[bank_name]["users"][username]['tlBalance'] -= total_price
        banks[bank_name]["users"][username]['valuableAmount'] += total_price
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} adet {currency_type} satın alındı.")
        print(f"{amount} adet {currency_type} başarıyla satın alındı.")
    else:
        print("Yetersiz bakiye!")

# Altın satımı
def sell_gold(username, bank_name):
    amount = int(input("Satmak istediğiniz altın miktarını girin: "))
    if amount <= banks[bank_name]["users"][username]['valuableAmount']:
        banks[bank_name]["users"][username]['tlBalance'] += amount * exchange_rates['GramAltın']
        banks[bank_name]["users"][username]['valuableAmount'] -= amount * exchange_rates['GramAltın']
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} gram altın satıldı.")
        print(f"{amount} gram altın başarıyla satıldı.")
    else:
        print("Yetersiz altın miktarı!")

# Coin satımı
def sell_coin(username, bank_name):
    amount = int(input("Satmak istediğiniz coin miktarını girin: "))
    if amount <= banks[bank_name]["users"][username]['coinAmount']:
        banks[bank_name]["users"][username]['tlBalance'] += amount * exchange_rates['Bitcoin']
        banks[bank_name]["users"][username]['coinAmount'] -= amount
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} adet coin satıldı.")
        print(f"{amount} adet coin başarıyla satıldı.")
    else:
        print("Yetersiz coin miktarı!")

# Döviz satımı
def sell_currency(username, bank_name):
    amount = int(input("Satmak istediğiniz döviz miktarını girin: "))
    if amount <= banks[bank_name]["users"][username]['valuableAmount']:
        banks[bank_name]["users"][username]['tlBalance'] += amount
        banks[bank_name]["users"][username]['valuableAmount'] -= amount
        banks[bank_name]["users"][username]['transactions'].append(f"{amount} birim döviz satıldı.")
        print(f"{amount} birim döviz başarıyla satıldı.")
    else:
        print("Yetersiz döviz miktarı!")

# Uygulamayı başlat
username, bank_name = login()

if username:
    while True:
        atm_menu(username, bank_name)
        choice = int(input("Lütfen bir işlem seçin: "))
        if choice == 1:
            show_profile(username, bank_name)
        elif choice == 2:
            print(f"Bakiyeniz: {banks[bank_name]['users'][username]['tlBalance']} TL")
        elif choice == 3:
            deposit(username, bank_name)
        elif choice == 4:
            withdraw(username, bank_name)
        elif choice == 5:
            show_account_summary(username, bank_name)
        elif choice == 6:
            print(bank_info)
        elif choice == 7:
            transfer(username, bank_name)
        elif choice == 8:
            eft(username, bank_name)
        elif choice == 9:
            buy_gold(username, bank_name)
        elif choice == 10:
            buy_coin(username, bank_name)
        elif choice == 11:
            buy_currency(username, bank_name)
        elif choice == 12:
            sell_gold(username, bank_name)
        elif choice == 13:
            sell_coin(username, bank_name)
        elif choice == 14:
            sell_currency(username, bank_name)
        elif choice == 15:
            print("Başarıyla çıkış yaptınız!")
            break
        elif choice == 16 and username in ["Diamond1", "Diamond2"]:
            show_users(bank_name)
        else:
            print("Geçersiz seçim. Lütfen geçerli bir seçenek seçin.")
else:
    print("Giriş yapılamadı, program sonlandırılıyor.")
