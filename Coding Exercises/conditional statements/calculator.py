print("""
******************
calculator

1.toplama
2.subsraction
3.multiplication
4.divison

******************
""")

a = int(input("first number:"))
b = int(input("second number:"))

operation = input("Select operation")

if operation == "1":
    print ("{} ile {} toplamı{} .".format(a,b,a+b))
elif operation == "2":
    print ("{} ile {}farkı {}. ".format(a,b,a-b))
elif operation == "3":
    print("{} ile {} çarpımı {}.".format(a,b,a*b))
elif operation == "4":
    print("{} ile {} bölümü {}.".format(a,b,a/b))
else:
    print("geçersiz işlem...")