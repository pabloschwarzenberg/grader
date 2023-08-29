def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']        

    lista = list(string)

    for i in range(len(lista)):
        if lista[i] in vocales:
            lista[i] = lista[i] + "p" + lista[i]

    string = ''.join(lista)

    return string
