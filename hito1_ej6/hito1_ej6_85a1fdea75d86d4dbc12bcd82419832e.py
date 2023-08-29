#Ordenar tres números
numeros = []
ingreso = int(input("ingrese un numero"))
numeros.append(ingreso)
ingreso2 = int(input("ingrese otro numero"))
numeros.append(ingreso2)
ingreso3 = int(input("ingrese un ultimo numero"))
numeros.append(ingreso3)
numeros.sort()
print(numeros)