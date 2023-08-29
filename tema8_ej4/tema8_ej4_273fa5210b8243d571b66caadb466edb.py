def rot13(s):
    abecedario = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
    codigo = ''
    for letra in s:
        indice = abecedario.find(letra)
        nueva_letra = abecedario[indice + 13]
        codigo += nueva_letra
    return codigo