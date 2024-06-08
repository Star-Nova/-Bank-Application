# Bank Application
# Döviz açıklaması ve Hesap özeti düzeltilecek
# Hesap Özeti gerektiği gibi çalışmıyor
# BANKA UYGULAMASI

# Kullanıcılar
PYT_bank_users = {
    "Gold4": {"surname": "Member", "password": "123", "tlBalance": 0, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold3": {"surname": "Member", "password": "123", "tlBalance": 10000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold2": {"surname": "Member", "password": "123", "tlBalance": 500000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Gold1": {"surname": "Member", "password": "123", "tlBalance": 1000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Diamond1": {"surname": "Member", "password": "123", "tlBalance": 100000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "Diamond2": {"surname": "Member", "password": "123", "tlBalance": 50000000, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

x_bank_users = {
    "XUser1": {"surname": "XMember", "password": "321", "tlBalance": 15000, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "XUser2": {"surname": "XMember", "password": "321", "tlBalance": 200000, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

y_bank_users = {
    "YUser1": {"surname": "YMember", "password": "231", "tlBalance": 7500, "coinAmount": 0, "valuableAmount": 0, "transactions": []},
    "YUser2": {"surname": "YMember", "password": "231", "tlBalance": 350000, "coinAmount": 0, "valuableAmount": 0, "transactions": []}
}

# Bankalar
banks = {
    "PYT Bankası": {"users": PYT_bank_users},
    "X Bankası": {"users": x_bank_users},
    "Y Bankası": {"users": y_bank_users}
}

# Değişkenlerin tanımlanması
altin_miktari = 0
Bitcoin_miktari = 0
Ethereum_miktari = 0
Tether_miktari = 0
Bnb_miktari = 0
Dolar_miktari = 0
Euro_miktari = 0
Sterlin_miktari = 0
KuveytDinarı_miktari = 0
Japonyeni_miktari = 0
ÇinYuanı_miktari = 0
accountSummary = []

# Banka hakkında bilgi
hakkinda = "PYT BANKASI 1999 yılında kuruldu. Her zaman güvenli sistemimizle paranızı muhafaza etmekteyiz. Bankamızın kurucusu Fernando'dur. 25 yıldır Türkiye'de milyonların paralarını güvenli bir şekilde muhafaza ettik. Bankamızı tercih ettiğiniz için teşekkür ederiz... "
Dolar = 33
Euro = 35
Japonyeni = 5
Sterlin = 40
KuveytDinarı = 100
ÇinYuanı = 6
GramAltın = 2500
ÇeyrekAltın = 4000
YarımAltın = 8000
TamAltın = 16000
Bitcoin = 2300000
Ethereum = 122000
Tether = 32
Bnb = 23000

# Kullanıcı girişi
def login():
    print("Lütfen giriş yapın.")
    giris_hakki = 5
    while giris_hakki > 0:
        kullanici_adi = input("Kullanıcı adınızı giriniz: ")
        surname = input("Soyadınızı giriniz: ")
        sifre = input("Şifrenizi giriniz: ")
        banka = input("Hangi bankaya aitsiniz? (PYT Bankası / X Bankası / Y Bankası): ")

        if banks.get(banka) and banks[banka]["users"].get(kullanici_adi) and banks[banka]["users"][kullanici_adi]["surname"] == surname and banks[banka]["users"][kullanici_adi]["password"] == sifre:
            print("Sisteme başarıyla giriş yaptınız!")
            accountSummary.append("Giriş")
            return kullanici_adi, surname, sifre, banka
        else:
            giris_hakki -= 1
            print("Şifre, kullanıcı adı, soyadı veya banka bilgileri yanlış! Tekrar deneyin!")

    print("Giriş hakkınız doldu. Sistem kapatılıyor.")
    return False, "", "", ""

# ATM menüsü
def atmMenu(kullanici_adi, soyadi, sifresi, banka):
    print("\n1. Profil")
    print("2. Bakiye sorgula ")
    print("3. Para yatır")
    print("4. Para çek")
    print("5. Hesap özeti")
    print("6. Banka hakkında bilgi al")
    print("7. Havale")
    print("8. Eft")
    print("9. Altın alımı")
    print("10. Coin alımı ")
    print("11. Döviz alımı")
    print("12. Altın satımı")
    print("13. Coin satımı ")
    print("14. Döviz satımı")  
    print("15. Çıkış yap")
    if kullanici_adi in ["Diamond1", "Diamond2"]:
        print("16. Kullanıcıları görüntüle")

# Geri kalan kısımları önceki kodlardan devam ettirerek doldurabiliriz.
# Kullanıcı profili
def showProfile(kullanici_adi, soyadi, sifresi, altin_miktari, coinAmount, valuableAmount, depositAmount):
    print("                               ")
    print(f"Profil Bilgileri:")
    print(f"Kullanıcı Adı: {kullanici_adi}")
    print(f"Soyadı: {soyadi}")
    print(f"Şifre: {sifresi}")
    print(f"Altın: {altin_miktari}")
    print(f"Coin: {coinAmount}")
    print(f"Döviz: {valuableAmount}")
    print(f"Para: {depositAmount}")
    for transaction in PYT_bank_users[kullanici_adi]["transactions"]:
        print(f"İşlem: {transaction}")


# Kullanıcıları görüntüleme
def showUsers():
    for user, info in PYT_bank_users.items():
        print(f"Kişi: {user}, Soy İsmi: {info['surname']}, Şifresi: {info['password']}, Para Miktarı: {info['tlBalance']}")


# Kullanıcı girişi yapılıyor
banks,loggedInUser, rightSurname, rightpassword = login()


# Kullanıcı girişi başarılı ise işlemler yapılıyor
if loggedInUser:
    while True:
        atmMenu(loggedInUser, rightSurname, rightpassword)
        choice = int(input("Lütfen bir işlem seçin: "))
        if choice == 1:
            showProfile(loggedInUser, PYT_bank_users[loggedInUser]["surname"], PYT_bank_users[loggedInUser]["password"], altin_miktari, PYT_bank_users[loggedInUser]["coinAmount"] , PYT_bank_users[loggedInUser]["valuableAmount"],PYT_bank_users[loggedInUser]['tlBalance'])
        elif choice == 15:
            print("Başarıyla çıkış yaptınız!")
            break
        if choice == 2:
            print(f"Bakiyeniz: {PYT_bank_users[loggedInUser]['tlBalance']}")
            accountSummary.append(f"Bakiye sorgulama. Bakiye: {PYT_bank_users[loggedInUser]['tlBalance']} TL ")
        elif choice == 3:
            depositAmount = int(input("Yatırılacak tutarı girin: "))
            PYT_bank_users[loggedInUser]['tlBalance'] += depositAmount
            print(f"Para yatırıldı: {depositAmount}. Yeni bakiye: {PYT_bank_users[loggedInUser]['tlBalance']}")
            PYT_bank_users[loggedInUser]["transactions"].append(f"{depositAmount} TL para yatırıldı.")
        elif choice == 4:
            withdrawAmount = int(input("Çekilecek tutarı girin: "))
            if withdrawAmount > PYT_bank_users[loggedInUser]['tlBalance']:
                print("Hesabınızda yeterli bakiye yok.")
            else:
                PYT_bank_users[loggedInUser]['tlBalance'] -= withdrawAmount
                print(f"Para çekildi: {withdrawAmount}. Yeni bakiye: {PYT_bank_users[loggedInUser]['tlBalance']}")
                PYT_bank_users[loggedInUser]["transactions"].append(f"{withdrawAmount} TL para çekildi.")
        elif choice == 5:
            for item in accountSummary:
                print(f"- {item}")
        elif choice == 6:
            print(hakkinda)
        elif choice == 7:
            receiver = input("Para göndermek istediğiniz kişinin kullanıcı adını girin: ")
            amount = int(input("Göndermek istediğiniz miktarı girin: "))
            if receiver in PYT_bank_users and amount <= PYT_bank_users[loggedInUser]['tlBalance']:
                PYT_bank_users[loggedInUser]['tlBalance'] -= amount
                PYT_bank_users[receiver]['tlBalance'] += amount
                print(f"{amount} TL, {receiver} hesabına başarıyla gönderildi.")
                PYT_bank_users[loggedInUser]["transactions"].append(f"{amount} TL, {receiver} hesabına havale yapıldı.")
                PYT_bank_users[receiver]["transactions"].append(f"{amount} TL, {loggedInUser} hesabından havale geldi.")
            else:
                print("Geçersiz işlem! Lütfen bilgilerinizi kontrol edin.")
        elif choice == 8:
            bank = input("EFT yapacağınız bankayı girin: ")
            receiver = input("EFT yapacağınız kişinin kullanıcı adını girin: ")
            amount = int(input("EFT yapmak istediğiniz miktarı girin: "))
            if bank == "PYT BANKASI" and receiver in PYT_bank_users and amount <= PYT_bank_users[loggedInUser]['tlBalance']:
                PYT_bank_users[loggedInUser]['tlBalance'] -= amount
                PYT_bank_users[receiver]['tlBalance'] += amount
                print(f"{amount} TL, {receiver} hesabına başarıyla EFT yapıldı.")
                PYT_bank_users[loggedInUser]["transactions"].append(f"{amount} TL, {receiver} hesabına EFT yapıldı.")
                PYT_bank_users[receiver]["transactions"].append(f"{amount} TL, {loggedInUser} hesabından EFT geldi.")
            else:
                print("Geçersiz işlem! Lütfen bilgilerinizi kontrol edin.")
        elif choice == 9:
            print(f"  Gram Altın Fiyatı :{GramAltın}TL\n  Çeyrek Altın Fiyatı :{ÇeyrekAltın}TL\n  Yarım Altın Fiyatı :{YarımAltın}TL\n  Tam Altın Fiyatı :{TamAltın}TL")
            try:
                altin_secenek = int(input("Hangi altını almak istiyorsunuz? (1-Gram Altın, 2-Çeyrek Altın, 3-Yarım Altın, 4-Tam Altın): "))
                miktar = int(input("Kaç adet almak istiyorsunuz? "))
                if altin_secenek in range(1, 5):
                    altin_fiyat = {"1": GramAltın, "2": ÇeyrekAltın, "3": YarımAltın, "4": TamAltın}[str(altin_secenek)]
                    if PYT_bank_users[loggedInUser]['tlBalance'] >= miktar * altin_fiyat:
                        altin_miktari += miktar
                        PYT_bank_users[loggedInUser]['tlBalance'] -= miktar * altin_fiyat
                        PYT_bank_users[loggedInUser]['valuableAmount'] += miktar * altin_fiyat
                        print(f"{miktar} adet altın satın aldınız.")
                        PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} adet altın satın alındı.")
                    else:
                        print("Yetersiz bakiye!")
                else:
                    print("Geçersiz seçim!")
            except ValueError:
                print("Geçersiz miktar! Lütfen sayısal bir değer girin.")
        elif choice == 10:
            print(f"  Bitcoin Fiyatı :{Bitcoin}TL\n  Ethereum Fiyatı :{Ethereum}TL\n  Tether Fiyatı :{Tether}TL\n  BNB Fiyatı :{Bnb}TL")
            try:
                coin_secenek = int(input("Hangi coini almak istiyorsunuz? (1-Bitcoin, 2-Ethereum, 3-Tether, 4-BNB): "))
                miktar = int(input("Kaç adet almak istiyorsunuz? "))
                coin_fiyat = {"1": Bitcoin, "2": Ethereum, "3": Tether, "4": Bnb}[str(coin_secenek)]
                if PYT_bank_users[loggedInUser]['tlBalance'] >= miktar * coin_fiyat:
                    PYT_bank_users[loggedInUser]['tlBalance'] -= miktar * coin_fiyat
                    PYT_bank_users[loggedInUser]['coinAmount'] += miktar
                    print(f"{miktar} adet coin satın aldınız.")
                    PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} adet coin satın alındı.")
                else:
                    print("Yetersiz bakiye!")
            except ValueError:
                print("Geçersiz miktar veya seçenek! Lütfen geçerli bir değer girin.")
        elif choice == 11:            
            print(f"Dolar Fiyatı: {Dolar}TL\nEuro Fiyatı: {Euro}TL\nSterlin Fiyatı: {Sterlin}TL\nKuveyt Dinarı Fiyatı: {KuveytDinarı}TL\nJapon Yeni Fiyatı: {Japonyeni}TL\nÇin Yuanı Fiyatı: {ÇinYuanı}TL")
            try:
                para_secenek = int(input("Hangi coini almak istiyorsunuz? (1-Dolar, 2-Euro, 3-Sterlin, 4-Kuveyt Dinarı, 5-Japon Yeni, 6-Çin Yuanı): "))
                miktar = int(input("Kaç adet almak istiyorsunuz? "))
                para_fiyat = {"1": Dolar, "2": Euro, "3": Sterlin, "4": KuveytDinarı, "5": Japonyeni, "6": ÇinYuanı}[str(para_secenek)]
                toplam_miktar = miktar * para_fiyat
                if PYT_bank_users[loggedInUser]['tlBalance'] >= toplam_miktar:
                    PYT_bank_users[loggedInUser]['tlBalance'] -= toplam_miktar
                    PYT_bank_users[loggedInUser]['valuableAmount'] += miktar
                    print(f"{miktar} adet döviz satın aldınız.")
                    PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} adet döviz satın alındı.")
                else:
                    print("Yetersiz bakiye!")
            except ValueError:
                print("Geçersiz miktar veya seçenek! Lütfen geçerli bir değer girin.")
# Altın, Coin ve Döviz Satımı              
        elif choice == 12:
            try:
                miktar = int(input("Satmak istediğiniz altın miktarını girin: "))
                if altin_miktari >= miktar:                    
                    altin_miktari -= miktar
                    PYT_bank_users[loggedInUser]['tlBalance'] += miktar * GramAltın
                    PYT_bank_users[loggedInUser]['valuableAmount'] -= miktar * GramAltın
                    print(f"{miktar} gram altını başarıyla sattınız.")
                    PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} gram altın satıldı.")
                else:
                    print("Yetersiz altın miktarı!")
            except ValueError:
                print("Geçersiz miktar! Lütfen sayısal bir değer girin.")
        elif choice == 13:
            try:
                miktar = int(input("Satmak istediğiniz coin miktarını girin: "))
                if PYT_bank_users[loggedInUser]['coinAmount'] >= miktar:                    
                    PYT_bank_users[loggedInUser]['tlBalance'] += miktar * Bitcoin
                    PYT_bank_users[loggedInUser]['coinAmount'] -= miktar
                    print(f"{miktar} adet coin başarıyla sattınız.")
                    PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} adet coin satıldı.")
                else:
                    print("Yetersiz coin miktarı!")
            except ValueError:
                print("Geçersiz miktar! Lütfen sayısal bir değer girin.")
        elif choice == 14:
            try:
                miktar = int(input("Satmak istediğiniz döviz miktarını girin: "))
                if PYT_bank_users[loggedInUser]['valuableAmount'] >= miktar:                    
                    PYT_bank_users[loggedInUser]['tlBalance'] += miktar
                    PYT_bank_users[loggedInUser]['valuableAmount'] -= miktar
                    print(f"{miktar} birim dövizi başarıyla sattınız.")
                    PYT_bank_users[loggedInUser]["transactions"].append(f"{miktar} birim döviz satıldı.")
                else:
                    print("Yetersiz döviz miktarı!")
            except ValueError:
                print("Geçersiz miktar! Lütfen sayısal bir değer girin.")


        elif choice == 16 and loggedInUser in ["Diamond1", "Diamond2"]:
            showUsers()
else:
    print("Geçersiz seçim. Lütfen geçerli bir seçenek seçin.")

