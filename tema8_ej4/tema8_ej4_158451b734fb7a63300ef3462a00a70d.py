def rot13(palabra):
    alfabetoLatino = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    palabra.lower()
    palabraRot = ""
    for letra in palabra:
        index = 0
        if (letra in alfabetoLatino):
            while (index < len(alfabetoLatino)):
                letraActual = alfabetoLatino[index]
                if (letra == letraActual):
                    indexUtil = index
                index += 1
            palabraRot += alfabetoLatino[(indexUtil + 13)%26]
    return palabraRot

print(rot13("hola"))