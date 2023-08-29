#Factores Primos
numero = int(input("Ingrese un número:"))

i = 2

while numero > 1 :
    if numero % i == 0 :
        print(i)
        numero = numero / i
    else :
        i = i + 1      