def jerigonzo(string):
    palabras = string
    vocales=["a","e","i","o","u"]
    conversion =""
    for i in palabras:

        conversion = conversion + i
        if(i in vocales):
            conversion = conversion+"p"+i
    return conversion
