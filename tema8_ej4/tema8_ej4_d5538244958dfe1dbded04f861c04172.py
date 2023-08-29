def rot13(s):
    tabla_traduccion = "abcdefghijklmnopqrstuvwxyz"
    tranducido = tabla_traduccion[13:]+tabla_traduccion[:13]
    rot_char = lambda c: tranducido[tabla_traduccion.find(c)] if tabla_traduccion.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )