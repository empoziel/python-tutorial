print("""
*******************************
Atm Makinesine Hoşgeldiniz.


işlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basın.
*******************************
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if (işlem == "q"):
        print("Yine Bekleriz")
        break
    elif(işlem =="1"):
        print("Bakiyeniz {} tldir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))

        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Miktarı Giriniz:"))

        if (bakiye - miktar < 0):
            print("Yetersiz Bakiye.")
            continue
        bakiye -= miktar

    else :
        print("Geçersiz işlem...")

