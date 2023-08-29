def rot13(palabra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    palabra.lower()
    palabraRot = ""
    for letra in palabra:
        idx = 0
        if (letra in alfabeto):
            while (idx < len(alfabeto)):
                letraActual = alfabeto[idx]
                if (letra == letraActual):
                    idxUtil = idx
                idx += 1
            palabraRot += alfabeto[(idxUtil + 13)%26]
    return palabraRot