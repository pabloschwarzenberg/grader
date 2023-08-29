#Descomponer un número
numero = int(input("Por favor, ingrese un numero de hasta 4 digitos: "))

c = numero % 1000
C = c / 100

d = numero % 100
D = d / 10

u = numero % 10

print(int(numero / 1000), "M", "+", int(C), "C", "+", int(D), "D", "+", int(u), "U")

