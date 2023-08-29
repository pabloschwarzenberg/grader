def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    i = 0
    j = 0

    # Recorrer las secuencias y realizar la alineación
    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            i += 1
            j += 1
        else:
            alineacion += "_"
            j += 1

    # Si quedan caracteres en secuencia2, agregar "_" al final
    while j < len(secuencia2):
        alineacion += "_"
        j += 1

    return alineacion

# Obtener las secuencias del usuario
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento de las secuencias
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(alineacion)
