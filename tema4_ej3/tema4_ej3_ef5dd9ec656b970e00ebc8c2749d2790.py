def jerigonzo(palabra):
    nueva_palabra = ""

    for letra in palabra :
        if letra in "AEIOUaeiou" :
            nueva_palabra += letra
            nueva_palabra += "p"
            
        nueva_palabra += letra

    return nueva_palabra
