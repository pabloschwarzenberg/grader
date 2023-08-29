def rot13(palabra):
    caract = "abcdefghijklmnopqrstuvwxyz"
    transf = caract[13:]+caract[:13]
    rot_caract = lambda c: transf[caract.find(c)] if caract.find(c)>-1 else c
    return ''.join( rot_caract(c) for c in palabra ) 