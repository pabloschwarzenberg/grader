#Descomponer un número
num = int(input())
lista = []
for i in str(num):
    lista.append(i)
lista.reverse()

# U
if len(lista) >= 1:
    lista[0] = lista[0] + "U"
if len(lista) >= 2:
    lista[1] = lista[1] + "D"
if len(lista) >= 3:
    lista[2] = lista[2] + "C"
if len(lista) >= 4:
    lista[3] = lista[3] + "M"
if len(lista) >= 5:
    exit("El numero debe ser de maximo 4 digitos")
lista.reverse()

# Print
if len(lista) >= 1:
    print(lista[0])
if len(lista) >= 2:
    print(lista[0], '+ ', end='')
    print(lista[1])
if len(lista) >= 3:
    print(lista[0], '+ ', end='')
    print(lista[1], '+ ', end='')
    print(lista[2])
if len(lista) >= 4:
    print(lista[0], '+ ', end='')
    print(lista[1], '+ ', end='')
    print(lista[2], '+ ', end='')
    print(lista[3])