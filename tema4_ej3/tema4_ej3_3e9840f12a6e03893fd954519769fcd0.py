
def jerigonzo(texto):
    contador=0
    contador2=0
    vocales=["a","e","i","o","u"]
    palabra=""
    palist=list(texto)
    final=len(palist)
    final2=len(palabra)
    while contador<final:
        palabra=palabra+texto[contador]
        if texto[contador]=="a" or texto[contador]=="A":
            palabra=palabra+"p"+"a"
        elif texto[contador]=="e" or texto[contador]=="E":
            palabra=palabra+"p"+"e"
        elif texto[contador]=="i" or texto[contador]=="I":
            palabra=palabra+"p"+"i"
        elif texto[contador]=="o" or texto[contador]=="O":
            palabra=palabra+"p"+"o"
        elif texto[contador]=="u" or texto[contador]=="U":
            palabra=palabra+"p"+"u"

        contador=contador+1
    return palabra

      