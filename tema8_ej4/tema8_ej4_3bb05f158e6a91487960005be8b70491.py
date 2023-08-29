def rot13(s):
    l = "abcdefghijklmnopqrstuvwxyz"
    trans = l[13:]+l[:13]
    rot_char = lambda c: trans[l.find(c)] if l.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )