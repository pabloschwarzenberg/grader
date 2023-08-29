#ENTRADA

def suma_divisores(s):
    d = []
    for i in range(1, s):
        if s%i == 0:
            i = d.append(i)
            
#PROCESAMIENTO
    adicion = 0
    for divisor in d:
        adicion = divisor + adicion
    if adicion == 1:
        valorprimo = True
        return adicion, valorprimo
#SALIDA
    else:
        valorprimo = False
        return adicion, valorprimo