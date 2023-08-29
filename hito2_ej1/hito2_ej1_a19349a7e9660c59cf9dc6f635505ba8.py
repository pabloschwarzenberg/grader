def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia1 = 0
    
    # Recorrer cada letra de la secuencia1
    for letra in secuencia1:
        # Verificar si el índice está dentro del rango válido para secuencia2
        if indice_secuencia1 < len(secuencia2):
            # Verificar si la letra es igual a la letra correspondiente en secuencia2
            if letra == secuencia2[indice_secuencia1]:
                secuencia_alineada += letra
                indice_secuencia1 += 1
            else:
                secuencia_alineada += "_"
        else:
            secuencia_alineada += "_"
    
    # Agregar las letras restantes de secuencia2
    secuencia_alineada += secuencia2[indice_secuencia1:]
    
    return secuencia_alineada

# Solicitar las secuencias al usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)
