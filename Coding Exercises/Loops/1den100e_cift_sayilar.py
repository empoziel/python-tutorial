for i in range(1,101):
    if (i % 2 != 0):
        continue
    x = []
    x.append(i)

    print("{}".format(x))

"""
çözümdeki yol = 
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)

"""