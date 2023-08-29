#Descomponer un número
num = int(input("Ingrese un numero de hasta 4 digitos: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10

print("{}M".format(um)  + "+{}C".format(c) + "+{}D".format(d) + "+{}U".format(u))