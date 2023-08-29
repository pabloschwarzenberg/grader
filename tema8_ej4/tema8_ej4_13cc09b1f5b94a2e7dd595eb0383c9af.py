def rot13(Palabra):
    AlfabetoLatino = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Palabra.lower()
    PalabraRot = ""
    for Letra in Palabra:
        index = 0
        if (Letra in AlfabetoLatino):
            while (index < len(AlfabetoLatino)):
                LetraActual = AlfabetoLatino[index]
                if (Letra == LetraActual):
                    indexUtil = index
                index += 1
            PalabraRot += AlfabetoLatino[(indexUtil + 13)%26]
    return PalabraRot

print(rot13("hola"))