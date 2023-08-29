#Factores Primos
numero = int(input())
for i in range(2,numero+1):
    while numero % i == 0:
        print(i)
        numero = numero / i      