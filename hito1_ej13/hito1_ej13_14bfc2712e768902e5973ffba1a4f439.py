#Factores Primos
numero_entero=int(input())
for i in range(2, numero_entero + 1):
    while numero_entero % i == 0:
            print(i)
            numero_entero = numero_entero / i