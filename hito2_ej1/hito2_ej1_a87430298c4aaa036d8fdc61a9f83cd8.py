def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0

    # Recorrer la primera secuencia
    for base1 in secuencia1:
        # Si la base en la segunda secuencia no coincide, insertar un guión bajo (_)
        if indice_secuencia2 >= len(secuencia2) or base1 != secuencia2[indice_secuencia2]:
            secuencia_alineada += "_"
        else:
            secuencia_alineada += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1

    # Si quedan bases en la segunda secuencia, agregarlas con guiones bajos
    if indice_secuencia2 < len(secuencia2):
        secuencia_alineada += secuencia2[indice_secuencia2:]

    return secuencia_alineada


# Obtener las dos secuencias de ADN del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento e imprimir el resultado
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)
