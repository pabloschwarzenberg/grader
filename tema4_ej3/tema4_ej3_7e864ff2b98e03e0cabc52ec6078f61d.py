def jerigonzo(string):
    resultado = []
    for letra in string:
        resultado.append(letra)
        if letra == "a":
            resultado.append("p")
            resultado.append("a")
        elif letra == "e":
            resultado.append("p")
            resultado.append("e")
        elif letra == "i":
            resultado.append("p")
            resultado.append("i")
        elif letra == "o":
            resultado.append("p")
            resultado.append("o")
        elif letra == "u":
            resultado.append("p")
            resultado.append("u")
    return "".join(resultado)         