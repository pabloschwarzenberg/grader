numero = int(input("Ingrese numero "))
for factor in range(2, numero + 1):
    if numero % factor == 0:
        print(str(factor))
        numero = numero / factor
