def rot13(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    trans = abc[13:]+abc[:13]
    rot_abc = lambda c: trans[abc.find(c)] if abc.find(c)>-1 else c
    return ''.join( rot_abc(c) for c in s )