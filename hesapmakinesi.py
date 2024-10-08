import math

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /, √, ^): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayıyı sıfıra bölemezsiniz!")
elif islem == "√":
    print("Birinci sayının karekökü:", math.sqrt(sayi1))
elif islem == "^":
    print("Birinci sayının ikinci sayı kadar üssü:", math.pow(sayi1, sayi2))
else:
    print("Geçersiz işlem.")
