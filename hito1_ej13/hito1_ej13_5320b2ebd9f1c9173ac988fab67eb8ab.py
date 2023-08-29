#Factores Primos
numero = int(input())
factor = 2

while numero > 1:
    if numero % factor == 0:
        print(factor)
        numero /= factor
    else:
        factor += 1
