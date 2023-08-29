def rot13(palabra):
    lista = list(palabra)
    for i in range(len(lista)):
        if ord(lista[i]) - 96 >= 14:
            lista[i] = chr(ord(lista[i]) - 13)
        else:
            lista[i] = chr(ord(lista[i]) + 13)
    palabra = ""
    for i in lista:
        palabra = palabra + i
    return palabra
   