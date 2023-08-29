def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0
    
    for nucleotido1 in secuencia1:
        if indice_secuencia2 < len(secuencia2) and nucleotido1 != secuencia2[indice_secuencia2]:
            alineacion += "_"
        else:
            if indice_secuencia2 < len(secuencia2):
                alineacion += secuencia2[indice_secuencia2]
                indice_secuencia2 += 1
            else:
                alineacion += "_"
    
    while indice_secuencia2 < len(secuencia2):
        alineacion += secuencia2[indice_secuencia2]
        indice_secuencia2 += 1
    
    return alineacion

# Obtener las secuencias del usuario
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento
alineacion_resultante = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(alineacion_resultante)
