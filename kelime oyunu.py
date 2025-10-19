from operator import truediv

from pyasn1_modules.rfc3852 import RecipientEncryptedKey

print("""
Kelime Oyunu

Kategoriler :

1-Meyve

2-Eşya

3-Renk
""")

import random

kelime_meyve = ["elma","armut","çilek","muz","kivi","portakal","mandalina","kavun","karpuz","erik"]
kelime_esya = ["kalem","silgi","askı","cüzdan","anahtar","telefon","masa","sandalye","yatak","bardak"]
kelime_renk = ["sarı","lacivert","mavi","kırmızı","turuncu","pembe","mor","siyah","beyaz","yeşil"]

while True:
    kategori = input("Kategori Seçiniz : ")

    if kategori == "1":
        kelime = random.choice(kelime_meyve)
        kategori_ad = "Meyve"
        print("Bu Kategorideki Kelimeler:", ", ".join(kelime_meyve))
    elif kategori == "2":
        kelime = random.choice(kelime_esya)
        kategori_ad = "Eşya"
        print("Bu Kategorideki Kelimeler:", ", ".join(kelime_esya))
    elif kategori == "3":
        kelime = random.choice(kelime_renk)
        kategori_ad = "Renk"
        print("Bu Kategorideki Kelimeler:", ", ".join(kelime_renk))
    else:
        print("Geçersiz kategori! Tekrar deneyin.")
        continue

    print(f"\nSeçilen kategori: {kategori_ad}")
    print(f"Kelimenin uzunluğu: {len(kelime)} harf")

    deneme = 0
    while True:
        tahmin = input("Tahmininiz: ").lower()
        deneme += 1
        if tahmin == kelime:
            print(f"Tebrikler! {deneme} denemede doğru bildiniz 🎉\n")
            break
        else:
            print("Yanlış Cevap! Tekrar Deneyiniz!")
