def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0

    # Iterar sobre los caracteres de la primera secuencia
    for caracter in secuencia1:
        # Si el caracter es distinto de "_", se agrega a la secuencia alineada
        if caracter != "_":
            secuencia_alineada += caracter
        else:
            # Si el caracter es "_", se agrega el caracter correspondiente de la segunda secuencia
            secuencia_alineada += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1

    # Agregar los caracteres restantes de la segunda secuencia si existen
    secuencia_alineada += secuencia2[indice_secuencia2:]

    return secuencia_alineada

# Pedir al usuario que ingrese las dos secuencias de ADN
secuencia1 = input()
secuencia2 = input()

# Alinear las secuencias y obtener el resultado
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir la secuencia alineada
print(secuencia_alineada)
      