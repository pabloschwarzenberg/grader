numeros = int(input("Dame la cantidad de numeros que debo sumar: "))
sumas = 0

for n in range(numeros+1):
    sumas = n + sumas
print(sumas)