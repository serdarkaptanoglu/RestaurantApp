from typing import Tuple

masalar = dict()
for a in range(20):
    masalar[a+1] = 0


def hesap_ekle():
    masa_no = int(input("Masa Numarasi Giriniz : "))
    bakiye = masalar[masa_no]
    hesap_tutari = float(input("Odenecek Ucreti Giriniz : "))
    guncel_bakiye = bakiye + hesap_tutari
    masalar[masa_no] = guncel_bakiye
    print("İsleminiz Tamamlandi..")


def hesap_odeme():
    masa_no = int(input("Masa Numarasi Giririniz : "))
    bakiye = masalar[masa_no]
    print(f"Masa {masa_no} hesabı {bakiye} TL")
    masalar[masa_no] = 0
    print("Hesap Odendi..")


def dosya_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi, "r", encoding="utf-8")
        veri = dosya.read()
        veri = veri.split("\n")
        veri.pop()
        dosya.close()
        for i in enumerate(veri):
            masalar[i[0]] = float(i[1])
    except FileNotFoundError:
        dosya = open(dosya_adi, "w", encoding="utf-8")
        dosya.close()
        print("Dosya Olusturuldu..")


def dosya_guncelle(dosya_adi):
    dosya = open(dosya_adi, "w", encoding="utf-8")
    for i in range(20):
        bakiye = str(masalar[i+1])
        dosya.write(bakiye + "\n")
    dosya.close()


def ana_islemler():
    dosya_kontrolu("bakiye.txt")
    while True:
        print("""
            -RestaurantApp Hoş Geldiniz-
        
        1)Masalari Goruntule
        2)Hesap Ekle
        3)Hesap Odeme
        Q)Çıkıs
    
        """)
        secim = input("Yapilacak islemi giriniz : ")
        if secim == "1":
            for i in range(20):
                print(f'Masa {i+1} icin hesap : {masalar[i+1]} TL')
        elif secim == "2":
            hesap_ekle()
        elif secim == "3":
            hesap_odeme()
        elif secim == "q" or secim == "Q":
            print("Cikis Yapiliyor..")
            quit()
        else:
            print("Hatali Giris Yapildi..")
        dosya_guncelle("bakiye.txt")
        input("Ana menuye donmek icin enter'a basiniz..")


ana_islemler()
