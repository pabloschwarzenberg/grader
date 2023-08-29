def jerigonzo(string):
    nuevapalabra = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p" + letra
            nuevapalabra.append(letra)
    nuevapalabra = "".join(nuevapalabra)
    return nuevapalabra