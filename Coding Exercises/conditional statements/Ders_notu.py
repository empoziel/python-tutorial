v1 = int(input("1. vize notu:"))
v2 = int(input("2. vize notu:"))
final = int(input("final notu:"))

not_ort = v1 * 3/10 + v2 * 3/10 + final * 4/10

if (not_ort >= 90):
    print("AA")
elif (not_ort >=85):
    print("BA")
elif (not_ort >=80):
    print("BB")
elif (not_ort >=75):
    print("CB")
elif (not_ort >=70):
    print("CC")
elif (not_ort >=65):
    print("DC")
elif (not_ort >=60):
    print("DD")
elif (not_ort >=55):
    print("DF")
elif (not_ort < 55):
    print("FF")
