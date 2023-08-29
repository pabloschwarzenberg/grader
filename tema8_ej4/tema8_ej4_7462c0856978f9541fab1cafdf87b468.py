def rot13(texto):
    n = 13
    letras = 'abcdefghijklmnopqrstuvwxyz'
    clave = ''
    for l in texto:
        if l in letras:
            pos_letra = letras.index(l)
            nueva_pos = (pos_letra + n) % len(letras)
            clave+= letras[nueva_pos]
        else:
            clave+= l
    return clave