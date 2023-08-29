def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    j = 0

    for i in range(len(secuencia1)):
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            j += 1
        else:
            alineacion += "_"
    
    alineacion += secuencia2[j:]  # Agregar los caracteres restantes de la segunda secuencia
    
    return alineacion

# Pedir al usuario que ingrese las secuencias
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Obtener la secuencia alineada
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Mostrar el resultado
print(secuencia_alineada)
    