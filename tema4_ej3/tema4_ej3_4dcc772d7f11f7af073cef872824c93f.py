def jerigonzo(string):
    palabra= str("")
    for letra in string:
        if letra in ("aeiou"):
            palabra += letra
            palabra += "p"
        palabra += letra

    return palabra
    
         