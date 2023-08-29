def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ''
    index_secuencia2 = 0

    # Iterar sobre la primera secuencia
    for letra in secuencia1:
        if letra == secuencia2[index_secuencia2]:
            # Si las letras coinciden, agregar la letra a la secuencia alineada
            secuencia_alineada += letra
            index_secuencia2 += 1
        else:
            # Si las letras no coinciden, agregar un guion bajo (_) a la secuencia alineada
            secuencia_alineada += '_'

    # Agregar los caracteres restantes de la segunda secuencia si es más larga que la primera
    if index_secuencia2 < len(secuencia2):
        secuencia_alineada += secuencia2[index_secuencia2:]

    return secuencia_alineada


# Obtener las secuencias del usuario
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento de las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)
