def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0
    
    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            alineacion += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            alineacion += "_"
        
    alineacion += secuencia2[indice_secuencia2:]
    
    return alineacion

# Obtener las secuencias de ADN
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar la alineación
resultado = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(resultado)
