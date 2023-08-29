def jerigonzo(string):
    traducida = ""
    for letra in string:

        if letra in "AEIOUaeiou":
            traducida = traducida + letra + "p" + letra
        else:
            traducida = traducida + letra
    return traducida
