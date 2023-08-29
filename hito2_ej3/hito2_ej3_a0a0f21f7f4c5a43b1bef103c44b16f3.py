cadena = input("cadena:")
n = int(input())
cadena_largo = len(cadena)
cont = 0
lista = []
cont = 0
lista_repetidas = []
for x in range(cadena_largo):
    if len(cadena[cont:])>=n:
        palabra=""
        for x in cadena[cont:]:
            if len(palabra)==3:
                break
            else:
                palabra+=x
        if palabra not in lista:
            lista.append(palabra)
        else:
            lista_repetidas.append(palabra)
    cont+=1

lista_nueva = [None]
for i in lista:
    if i not in lista_repetidas:
        if lista_nueva[0] == None:
            lista_nueva.pop()
        lista_nueva.append(i)

if lista_nueva[0] == None:
    lista_nueva.pop()
    lista_nueva.append("ninguna")
    print(lista_nueva)
else:
    for i in lista_nueva:
        print(i)
