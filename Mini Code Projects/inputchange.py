a = int(input("a:"))
b = int(input("b:"))

print("girilen değer\na: {}\nb :{}".format(a,b))

a,b = b,a

print ("değiştirilen değer\na: {}\nb :{}".format(a,b))