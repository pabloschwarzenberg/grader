def rot13(s):
    carac = "abcdefghijklmnopqrstuvwxyz"
    transforma = carac[13:]+carac[:13]
    rot_carac = lambda c: transforma[carac.find(c)] if carac.find(c)>-1 else c
    return ''.join( rot_carac(c) for c in s )
           