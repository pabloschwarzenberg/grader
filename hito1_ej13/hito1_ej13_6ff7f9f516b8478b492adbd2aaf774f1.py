#Factores Primos
numero = int(input())
while numero % 2 == 0:
    print(2)
    numero = numero // 2
i = 3
while i * i <= numero:
    while numero % i == 0:
        print(i)
        numero = numero // i
    i = i + 2
if numero > 2:
    print(numero)      