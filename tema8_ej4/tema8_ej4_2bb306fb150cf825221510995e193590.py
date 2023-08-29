def rot13(s):
    atributo = "abcdefghijklmnopqrstuvwxyz"
    trans = atributo[13:]+atributo[:13]
    rot_atributo = lambda c: trans[atributo.find(c)] if atributo.find(c)>-1 else c
    return ''.join( rot_atributo(c) for c in s )