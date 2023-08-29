import random
def ocultar_letras(palabra, cantidad):
    a = 0
    palabra = list(palabra)
    palabraN = ''
    while a < cantidad:
        num = random.randint(0, len(palabra) - 1)
        if palabra[num] != '_':
            palabra[num] = '_'
            a += 1
        else:
            pass
    for a in palabra:
        palabraN += a
    return palabraN
def revisar_letra(palabra, ps, letra):
    a = 0
    palabraF = ''
    ps = list(ps)
    palabra = list(palabra)
    while a < len(palabra):
        if letra == palabra[a]:
            ps[a] = letra
            a += 1
        else:
            a += 1
    for z in ps:
        palabraF += z
    palabraF.strip(' ')
    return palabraF   