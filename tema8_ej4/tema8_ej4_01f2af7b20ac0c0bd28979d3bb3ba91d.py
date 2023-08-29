def rot13(cifrado):
    words = "abcdefghijklmnopqrstuvwxyz"
    cambio = words[13:]+words[:13]
    rotacion_palabra = lambda c: cambio[words.find(c)] if words.find(c)>-1 else c
    return ''.join( rotacion_palabra(c) for c in cifrado )           