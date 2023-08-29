def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    trans = letras[13:]+letras[:13]
    rot_char = lambda c: trans[letras.find(c)] if letras.find(c)>-1 else c
    return ''.join( rot_char(c) for c in palabra )

print(rot13('luis'))
           