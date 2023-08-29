def jerigonzo(palabra):
    nueva_p = ""

    for letra in palabra :
        if letra in "AEIOUaeiou" :
            nueva_p += letra
            nueva_p += "p"
            
        nueva_p += letra

    return nueva_p
