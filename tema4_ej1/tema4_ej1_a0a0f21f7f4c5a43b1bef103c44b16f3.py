import random

def ocultar_letras(palabra,cantidad):
    lista = []
    for i in palabra:
        lista.append(i)
    cont = 0
    while cantidad != cont:
        pos = random.randint(0,len(lista)-1)
        val = lista[pos]
        val = lista.index(val)
        while lista[val] == "_":
            pos = random.randint(0,len(palabra)-1)
            val = lista[pos]
            val = lista.index(val)
        lista[val] = "_"
        cont +=1
    palabra = ""
    for i in lista:
        palabra+=i
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    lista = []

    for i in palabra:
        lista.append(i)
    listaoculta = []
    for i in palabra_secreta:
        listaoculta.append(i)

    if len(letra) == len(lista):
        for x in range(len(palabra)):
            if letra[x] == lista[x]:
                listaoculta[x] = lista[x]
            else:
                return palabra_secreta
    else:
        for i in range(len(lista)):
            if lista[i] == letra:
                listaoculta[i] = letra

    palabra_nueva = ""
    for x in listaoculta:
        palabra_nueva+=x
    return palabra_nueva