def jerigonzo(string):
    letras = string
    vocales=["a","e","i","o","u"]
    convertir =""
    for i in letras:

        convertir = convertir + i
        if(i in vocales):
            convertir = convertir +"p"+i
    return convertir       