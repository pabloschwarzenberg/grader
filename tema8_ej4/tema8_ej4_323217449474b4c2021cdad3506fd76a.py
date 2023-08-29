def rot13(s):
    letras = "abcdefghijklmnopqrstuvwxyz"
    conver = letras[13:]+letras[:13]
    con_letra = lambda c: conver[letras.find(c)] if letras.find(c)>-1 else c
    return ''.join( con_letra(c) for c in s )