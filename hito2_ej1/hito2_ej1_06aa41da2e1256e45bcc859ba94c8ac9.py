def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    index_secuencia1 = 0
    
    for caracter in secuencia2:
        if index_secuencia1 >= len(secuencia1):
            secuencia_alineada += caracter
        elif caracter == secuencia1[index_secuencia1]:
            secuencia_alineada += caracter
            index_secuencia1 += 1
        else:
            secuencia_alineada += "_"
    
    return secuencia_alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")
    
    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    
    print(secuencia_alineada)
