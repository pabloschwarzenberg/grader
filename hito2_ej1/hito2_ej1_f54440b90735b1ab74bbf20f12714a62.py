def alineamiento_secuencias (secuencia1, secuencia2):
    alineamiento = ""
    
    n = 0
    for a in secuencia1:
        if secuencia2[n] == a:
            alineamiento += a
            n += 1
        else:
            alineamiento += "_"
    if len(secuencia2[n:]) > 0:
        alineamiento += secuencia2[n:]


    print(alineamiento)
    
secuencia1 = input()
secuencia2 = input()
alineamiento_secuencias(secuencia1, secuencia2)