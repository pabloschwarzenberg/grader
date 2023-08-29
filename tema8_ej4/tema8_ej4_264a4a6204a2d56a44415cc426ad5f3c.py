def rot13(palabra):
    n = 13
    Lista = list(frase)
    largo = len(Lista)
    i = 0
    for letra in Lista:
        if (letra == "á"):
            Lista[i] = "a"
        elif (letra == "é"):
            Lista[i] = "e"
        elif (letra == "í"):
            Lista[i] = "i"
        elif (letra == "ó"):
            Lista[i] = "o"
        elif (letra == "ú"):
            Lista[i] = "u"
        elif (letra == "Á"):
            Lista[i] = "A"
        elif (letra == "É"):
            Lista[i] = "E"
        elif (letra == "Í"):
            Lista[i] = "I"
        elif (letra == "Ó"):
            Lista[i] = "O"
        elif (letra == "Ú"):
            Lista[i] = "U"
        i = i + 1
    lstEncriptada = []
    for letra in Lista:
        if letra.isalpha():
            if ("A" <= letra <= "z"):
                lstEncriptada.append(chr((ord(letra) - 97 + n) % 26 + 97))
            else:
                lstEncriptada.append(letra + n)
    i = i + 1
    strEncriptado = "".join(lstEncriptada)
    return strEncriptado
frase = "frase"
if frase == "frase":
    frase = input("Ingresa una frase: ")
    print(rot13(frase))