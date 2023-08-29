def jerigonzo(string):
    vocales = ['a','e','i','o','u']
    lista = []
    for i in string:
        if vocales.count(i):
            i = i+'p'+i
        lista.append(i)
    return ''.join(lista)