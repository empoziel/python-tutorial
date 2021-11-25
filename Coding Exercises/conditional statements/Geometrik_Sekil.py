şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

if (şekil == "Dikdörtgen"):
    print("lütfen kenarları sırasıyla giriniz.")
    a = int (input("kenar-1:"))
    b = int(input("kenar-2:"))
    c = int(input("kenar-3:"))
    d = int(input("kenar-4:"))

    if (a == b and a== c and a==d):
        print("Kare")
    elif(a==c and b== d):
        print("dikdörtgen")
    else:
        print("dörtgen")

elif(şekil == "Üçgen"):
    a = int(input("kenar-1:"))
    b = int(input("kenar-2:"))
    c = int(input("kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b == c):
            print("Eşkenar üçgen")
        elif((a==b and a !=c) or (a==c and a != b) or (b==c and b!=a)):
            print("İkizkenar üçgen")
        else:
            print("çeşitkenar üçgen")
    else:
        print("üçgen belirtmiyor")
else:
    print("geçersiz şekil")