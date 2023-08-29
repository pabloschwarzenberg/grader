def rot13(txt):
    encriptador = ""
    espacio = 13
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(txt)):
        for j in range(len(letras)):
            if txt[i] == letras[j]:
                if j + espacio > 25:
                    diff = (j + espacio) - 25
                    encriptador = encriptador + (letras[diff -1])
                else:
                    encriptador = encriptador + (letras[j+espacio])
    return encriptador
           