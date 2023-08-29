def rot13(s):
    letrasabecedario = "abcdefghijklmnopqrstuvwxyz"
    transformacion = letrasabecedario[13:]+letrasabecedario[:13]
    rot_letras = lambda c: transformacion[letrasabecedario.find(c)] if letrasabecedario.find(c)>-1 else c
    return ''.join( rot_letras(c) for c in s ) 