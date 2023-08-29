# alineamiento de secuencias 

def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0
    
    # Recorrer cada carácter de la primera secuencia
    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            secuencia_alineada += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            secuencia_alineada += "_"
  # Añadir los caracteres restantes de la segunda secuencia
    secuencia_alineada += secuencia2[indice_secuencia2:]
    
    return secuencia_alineada

# Solicitar entrada al usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)
