#Factores Primos
numero = int(input())
for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            print(i)
            numero //= i
if numero > 1:
        print(numero)