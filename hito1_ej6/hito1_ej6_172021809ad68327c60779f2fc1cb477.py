#Ordenar tres números
numeros = []

for i in range(0,3):
    a = int(input("Escriba los numeros: "))
    numeros.append(a)


for i in range(0,3):
    auxiliar = numeros[i]
    j = i - 1
    while j >= 0 and auxiliar < numeros[j]:
        numeros[j + 1] = numeros[j]
        j -= 1
    numeros[j + 1] = auxiliar
print('Numeros: ', numeros)
print('')