palabra = input("Ingrese secuencia: ")
palabra = palabra.upper()
número = int(input("Ingrese número: "))
lista = []
z = ""
for i in range(len(palabra)):
    k = i
    while len(z) < número:
        z = z + palabra[k]
        k = k + 1
        if k >= len(palabra):
            z = 9
            break
    if z != 9:
        lista.append(z)
    z = ""
print(lista)
i = 1
for s in lista:
    d = lista.count(s)
    if d > 1:
        while i <= d:
            a = lista.index(s)
            del lista[a]
            i = i + 1
    elif d == 0:
        continue
if len(lista) == 0:
    print("Ninguna")
if len(lista) != 0:
    for m in lista:
        print(m)    