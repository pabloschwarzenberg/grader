def rot13(palabra):
    palabra = list(palabra)
    letras = list("abcdefghijklmnñopqrstuvwxyz")
    for i in range(len(palabra)) :
        for j in range(len(letras)) :
            if palabra[i] == letras[j] :
                if j + 13 <= len(letras) :
                    palabra[i] = letras[j + 13]
                else :
                    palabra[i] = letras[13 - (27 - j)]
    return ''.join(palabra)