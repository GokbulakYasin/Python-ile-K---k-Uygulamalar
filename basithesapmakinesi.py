x = int(input("Birinci sayıyı girin. : "))
y = int(input("İkinci sayıyı girin. : "))
islem = input("Yapmak istediğiniz işlemi seçin |+|-|x|:| : ")

if islem == "+":
    print(x+y)
elif islem == "-":
    print(x-y)
elif islem == "x":
    print(x*y)
elif islem == ":":
    print(x/y)
else:
    print("Lütfen geçerli bir sayı ve işlem giriniz.")