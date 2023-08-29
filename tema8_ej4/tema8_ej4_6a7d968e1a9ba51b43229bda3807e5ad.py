def rot13(palabra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    formarot = ""
    for letra in palabra:
        cont = 0
        if (letra in alfabeto):
            while (cont < len(alfabeto)):
                letraActual = alfabeto[cont]
                if (letra == letraActual):
                    contshafa = cont
                cont = cont + 1
            formarot = formarot + alfabeto[(contshafa + 13)%26]
    return formarot
    
