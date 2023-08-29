numeros = []
numero = eval(input("Numero: "))
if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    numeros.append(numero)
else:
    for i in range(2, numero):
        if numero % i == 0:
            numeros.append(i)
            numero = numero/i
for i in range(len(numeros)):
    print(numeros[i], end="\t")
    print()