#Descomponer un número
n = int(input("Ingrese número de máximo 4 dígitos: "))
a = (n // 1000)
c =((n % 1000) // 100)
d =((n % 100) // 10)
u = (n % 10)
if n > 999:
    print(str(a) + "M+" + str(c) + "C+" + str(d) + "D+" + str(u) + "U")
if n > 99:
    print(str(c) + "C+" + str(d) + "D+" + str(u) + "U")
if n > 9:
    print(str(d) + "D+" + str(u) + "U")
if n >= 0:
    print(str(u) + "U")