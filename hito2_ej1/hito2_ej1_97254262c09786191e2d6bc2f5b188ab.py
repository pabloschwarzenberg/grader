def alinear_secuencias(secuencia1, secuencia2):
    # Inicializar el índice para recorrer la segunda secuencia
    i = 0
    
    # Inicializar la secuencia alineada con espacios en blanco
    secuencia_alineada = ''
    
    # Recorrer la primera secuencia
    for nucleotido in secuencia1:
        # Si el índice está dentro del rango de la segunda secuencia y los nucleótidos coinciden
        if i < len(secuencia2) and nucleotido == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += '_'
    
    # Si quedan nucleótidos en la segunda secuencia, agregarlos al final de la secuencia alineada
    if i < len(secuencia2):
        secuencia_alineada += secuencia2[i:]
    
    return secuencia_alineada

# Obtener las secuencias del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Alinear las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir la secuencia alineada
print(secuencia_alineada)
