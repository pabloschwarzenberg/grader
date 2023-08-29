def jerigonzo(string):
    resultado = ""
    for letra in string:
        resultado += letra
        if letra.lower() in "aeiou":
            resultado += "p" + letra
    return resultado