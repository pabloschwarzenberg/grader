def rot13(palabra):
    alfabeto1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alfabeto2 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    lista_palabra = list(palabra)
    palabra_encriptada = []
    for i in range(0, len(lista_palabra)):
        for j in range(0, len(alfabeto1)):
            if lista_palabra[i] == alfabeto1[j]:
                letra_cambiada = alfabeto2[j]
                palabra_encriptada.append(letra_cambiada)
    return "".join(palabra_encriptada)