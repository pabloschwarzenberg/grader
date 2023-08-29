import random as rnd

def ocultar_letras(palabra,cantidad):
    numaleatorios = []
    palabra_secreta = []
    n = 0
    while n < cantidad:
        nshaya = int(rnd.randrange(0,len(palabra)))
        if nshaya not in numaleatorios:
            numaleatorios.append(nshaya)
            n = n + 1
    for numero in range(0, len(palabra)):
        if (numero in numaleatorios):
            palabra_secreta.append("_")
        else:
            palabra_secreta.append(palabra[numero])
    return palabra_secreta

def revisar_letra(palabra_secreta,palabra,letra):
    for numero in range(0, len(palabra)):
        if (letra == palabra[numero]):
            palabra_secreta[numero] = letra
    return palabra_secreta
   