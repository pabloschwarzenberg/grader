def jerigonzo(palabra):
    traducido = ""
    for letra in palabra:
        if letra == "a":
            traducido = traducido + letra + "p" + letra
        elif letra == "e":
            traducido = traducido + letra + "p" + letra
        elif letra == "i":
            traducido = traducido + letra + "p" + letra
        elif letra == "o":
            traducido = traducido + letra + "p" + letra
        elif letra == "u":
            traducido = traducido + letra + "p" + letra
        else:
            traducido = traducido + letra
    return traducido

if __name__ == "__main__":
    pass
         