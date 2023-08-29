def rot13(s):
    linea = "abcdefghijklmnopqrstuvwxyz"
    trans = linea[13:]+linea[:13]
    linea_rot = lambda c: trans[linea.find(c)] if linea.find(c)>-1 else c
    return ''.join( linea_rot(c) for c in s )
           