import random

def ocultar_letras(palabra,cantidad):
    i = 0
    while i<cantidad:
        lo = random.choice(palabra)
        if lo != '_':
            plo = palabra.index(lo)
            palabra = palabra.replace(palabra[plo],'_',1)
            i = i+1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    i = 0
    palabra_final = []
    for letraps in palabra_secreta:
        pletraps = palabra_secreta.find(letraps, i, len(palabra_secreta))
        if letraps==letra:
            palabra_final.append(letraps)
        else:
            palabra_final.append(palabra[pletraps])
        i = pletraps+1
    palabra_entrega = ''.join(palabra_final)
    return palabra_entrega