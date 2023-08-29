def jerigonzo(string):
    lista = string
    vocales=["a","e","i","o","u"]
    frase_nueva =""
    for i in lista:

        frase_nueva = frase_nueva + i
        if(i in vocales):
            frase_nueva = frase_nueva+"p"+i
    return frase_nueva