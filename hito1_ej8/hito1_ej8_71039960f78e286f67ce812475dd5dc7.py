#Descomponer un número
num = int(input("Introduzca un numero: "))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10

print(("{}M".format(M)), "+" + (" {}C".format(C)), "+" + (" {}D".format(D)), "+" + (" {}U".format(U)))
