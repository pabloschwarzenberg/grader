def rot13(s):
    letra = "abcdefghijklmnopqrstuvwxyz"
    trans = letra[13:]+letra[:13]
    rot_char = lambda c: trans[letra.find(c)] if letra.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )

print(rot13('cesar'))