#Descomponer un número
e = int(input("ingrese numero "))
c1 = e % 10
c2 = int((e % 100) / 10)
c3 = int((e % 1000) / 100)
c4 = int((e - (e % 1000)) / 1000)
c5 = "M+"
c6 = str(c4) + c5
c7 = "C+"
c8 = str(c3) + c7
c9 = "D+"
c10 = str(c2) + c9
c11 = "U"
c12 = str(c1) + c11
print(str(c6) + str(c8) + str(c10) + str(c12))     