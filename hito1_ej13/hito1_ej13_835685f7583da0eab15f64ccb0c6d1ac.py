num = int(2)
numero = int(input("Ingresa el número a calcular factores primos: "))

while (numero != 1):

    if (numero % num == 0):
        print(str(num)+" ")
        numero = numero / num

    else:
        num = num + 1