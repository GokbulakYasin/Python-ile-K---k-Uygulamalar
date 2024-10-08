import random

rastgele_sayi = random.randint(1, 100)
tahmin = None

while tahmin != rastgele_sayi:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if tahmin < rastgele_sayi:
        print("Daha büyük bir sayı tahmin et.")
    elif tahmin > rastgele_sayi:
        print("Daha küçük bir sayı tahmin et.")
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
