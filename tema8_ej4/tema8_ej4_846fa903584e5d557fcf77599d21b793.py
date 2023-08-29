def rot13(s):
    palabras = "abcdefghijklmnopqrstuvwxyz"
    transicion = palabras[13:]+palabras[:13]
    rotacion_palabra = lambda c: transicion[palabras.find(c)] if palabras.find(c)>-1 else c
    return ''.join( rotacion_palabra(c) for c in s )
           