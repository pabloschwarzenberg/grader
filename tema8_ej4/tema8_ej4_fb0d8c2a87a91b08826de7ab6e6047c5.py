def rot13(palabra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    largo = len(palabra)
    q = 0
    letras = ""
    while (q < largo):
        b = palabra[0]
        palabra = palabra[1:]
        c = alfabeto.find(b)
        c = c + 13
        if (c >= 26):
            c = c - 26
            d = alfabeto[c]
            q = q + 1
            letras = letras + d
        else:
            d = alfabeto[c]
            q = q + 1
            letras = letras + d
    while (q >= largo):
        return letras

