def jerigonzo(string):
    vocales="aeiou"
    i=0
    lista=list(string)
    while i<len(string):
        if lista[i] in vocales:
            lista[i]=str(lista[i])+"p"+str(lista[i])
            i = i + 1
        else:
            lista[i]=lista[i]
            i = i + 1

    string="".join(lista)

    return string


         