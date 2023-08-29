s = str(input("Ingrese un string: "))
n = int(input("Ingrese un entero: "))
lista = []
for i in range(len(s)):
    if i+n <= len(s):
        lista.append(s[i:i+n])
lista.sort()
lista2 = []
for i in range(len(lista)):
    if lista.count(lista[i]) == 1:
        lista2.append(lista[i])
if len(lista2) == 0:
    print("ninguna")
else:
    for i in range(len(lista2)):
        print(lista2[i])