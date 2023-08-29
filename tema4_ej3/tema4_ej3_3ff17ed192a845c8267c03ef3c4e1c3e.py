def jerigonzo(string):
    palabra = ""
    for letra in string:
        palabra += letra
        if letra.lower() in "aeiou":
            palabra += "p" + letra
    return palabra
mensaje= jerigonzo('que pa mi shan')
print(mensaje)
         