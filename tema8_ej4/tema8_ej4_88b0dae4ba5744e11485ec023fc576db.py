alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]


def rot13(palabra):
    listaindices = []
    palabra = palabra.lower()
    palabralista = list(palabra)
    for i in palabralista:
        listaindices.append(alfabeto.index(i) + 13)
    contadorin_pompin = 0
    for i in listaindices:
        if i > 25:
            listaindices[contadorin_pompin] = i - 26
        contadorin_pompin += 1
    contador = 0
    for i in palabralista:
        palabralista[contador] = alfabeto[listaindices[contador]]
        contador += 1
    nueva = "".join(palabralista)
    return nueva     