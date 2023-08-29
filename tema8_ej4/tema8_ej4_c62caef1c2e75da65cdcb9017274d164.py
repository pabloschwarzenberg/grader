def rot13(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    sil = abc[13:]+abc[:13]
    rot_abc = lambda c: sil[abc.find(c)] if abc.find(c)>-1 else c
    return ''.join( rot_abc(c) for c in s )