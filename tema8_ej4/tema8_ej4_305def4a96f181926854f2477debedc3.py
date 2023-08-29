def rot13(s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    traduccion = alfabeto[13:] + alfabeto[:13]
    rot_trad = lambda c: traduccion[alfabeto.find(c)] if alfabeto.find(c)>-1 else c
    return ''.join( rot_trad(c) for c in s ) 