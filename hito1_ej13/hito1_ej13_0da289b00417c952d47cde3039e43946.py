#Factores Primos
print("DESCOMPOSICIÓN EN NÚMEROS PRIMOS")
numero = int(input("Escriba un número entero mayor que 1: "))
while numero <= 1:
    numero = int(input(f"{numero} no es mayor que 1. Inténtelo de nuevo: "))
copia = numero

print("Descomposición en factores primos:");print(end="")
for i in range(2, numero + 1):
    while copia % i == 0:
        copia = copia // i
        print(i);print( end="")      