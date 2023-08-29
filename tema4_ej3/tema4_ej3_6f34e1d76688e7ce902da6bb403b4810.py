def jerigonzo(palabra):
    traslado = ""    
    for letra in palabra:
        if letra in "AEIOUaeiou":
            traslado += letra
            traslado += "p"
        traslado += letra
    return traslado
