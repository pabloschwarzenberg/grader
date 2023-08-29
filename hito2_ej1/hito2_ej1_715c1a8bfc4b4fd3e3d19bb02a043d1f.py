def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ''
    i = 0
    
    for nucleotido in secuencia1:
        if i < len(secuencia2) and nucleotido == secuencia2[i]:
            secuencia_alineada += nucleotido
            i += 1
        else:
            secuencia_alineada += '_'
    
    if i < len(secuencia2):
        secuencia_alineada += secuencia2[i:]
    
    return secuencia_alineada

secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)
