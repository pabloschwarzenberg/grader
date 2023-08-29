def jerigonzo(string):
    letras1 = string
    vocales=["a","e","i","o","u"]
    conver =""
    for i in letras1:

        conver = conver + i
        if(i in vocales):
            conver = conver+"p"+i
    return conver