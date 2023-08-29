numero = int(input("ingrese numero: "))

i = 2
factores = []
while i * i <= numero:
    if numero % i:
        i += 1
    else:
        numero //= i
        factores.append(i)
if numero > 1:
    factores.append(numero)


for x in factores:
    print(x)