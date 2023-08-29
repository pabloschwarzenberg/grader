import math

def decodificar(mensaje):
    l = mensaje.split(",")
    l_reales = []
    l_letras = []
    i = 0
    while i < len(l):
        j = 0
        num = 0
        while j < len(l[i]):
            num = num + (int(l[i][j]) * (2**((len(l[i])-1)-j)))
            j+=1
        i+=1
        l_reales.append(num)
    print(l_reales)
    i = 0
    while i < len(l_reales):
        l_letras.append(chr(l_reales[i]))
        i += 1
    return "".join(l_letras)