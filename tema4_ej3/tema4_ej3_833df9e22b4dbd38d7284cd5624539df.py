def jerigonzo(string):
    stringM=string.lower()
    vocales=["a","e","i","o","u"]
    salida=""
    for letra in stringM:
        i=0
        while i<len(vocales):
            if letra is vocales[i]:
                salida+=str(letra+"p"+letra)
                i=len(vocales)
            else:
                i+=1
        f=0
        retificador=0
        while f<len(vocales):
            if letra is vocales[f]:
                retificador+=1
            f+=1
        if retificador==0:
            salida+=str(letra)

    return salida

