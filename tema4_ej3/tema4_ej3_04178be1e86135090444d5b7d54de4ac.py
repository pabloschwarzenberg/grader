def jerigonzo(string):
    cadena = ""
    for letra in string:
        if letra in "AEIOUaeiou":
           cadena += letra 
           cadena += "p" #agregar p despues de la vocal
           cadena += letra
        else:
            cadena += letra
    return cadena