"""
2. dereceden bir bilinmeyeli denklemin köklerini bulma

denklem: ax^2 + bx +c

delta : b ** 2 -4 * a * c
Birinci Kök : (-b - delta ** 0.5 ) / (2*a)
İkinci Kök : (-b + delta ** 0.5 ) / (2*a)
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("Birinci kök: {}\nİkinci kök: {}".format(x1,x2))
