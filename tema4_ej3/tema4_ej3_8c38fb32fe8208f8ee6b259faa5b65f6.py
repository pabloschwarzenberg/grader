def jerigonzo(string):
    return string
def jerigonzo(frase):
    cont=0
    stri=""
    vocales=["a","e","i","o","u"]
    while cont <len(frase):
        if frase[cont]in vocales:
            stri=stri+frase[cont]+"p"+frase[cont]
        else:
            stri=stri+frase[cont]
        cont=cont+1
    return stri

      