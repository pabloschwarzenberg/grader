def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0
    
    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            secuencia_alineada += caracter
            indice_secuencia2 += 1
        else:
            secuencia_alineada += "_"
    
    secuencia_alineada += secuencia2[indice_secuencia2:]
    return secuencia_alineada


secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")


secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)


print(secuencia_alineada)