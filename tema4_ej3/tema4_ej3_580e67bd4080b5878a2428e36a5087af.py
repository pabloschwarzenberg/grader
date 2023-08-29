def jerigonzo(palabra):
    
    translado = ""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            translado += letra
            #agregar p despues de la vocal
            translado += "p"
        #repetir vocal
        translado += letra

    return translado