def rot13(s):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    trans = caracteres[13:]+ caracteres[:13]
    rot_caracteres = lambda c: trans[caracteres.find(c)]
    if caracteres.find(c)>-1
    else c
    return ''.join( rot_caracteres c)

