"""
fibonacci serisi bir sayıyı önceki iki sayının toplamı şeklinde oluşur.


"""

a = 1
b = 1

fibonacci = []

for i in range(20):
    a,b = a,a+b

    fibonacci.append(b)

print(fibonacci)