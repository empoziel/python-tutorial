
boy = float(input("boy:"))
kilo = float(input("kilo:"))

x = kilo/(boy ** 2)

if (x < 18.5):
    print("zayıf")
elif (18.5 <= x < 25):
    print("normal")
elif (25 <= x < 30):
    print("fazla kilolu")
else:
    print("obez")


