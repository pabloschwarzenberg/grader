def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    index_secuencia2 = 0
    
    # Recorrer la secuencia1 caracter por caracter
    for char in secuencia1:
        if char == secuencia2[index_secuencia2]:
            # Si los caracteres coinciden, agregarlo a la secuencia alineada
            secuencia_alineada += char
            index_secuencia2 += 1
        else:
            # Si los caracteres no coinciden, agregar un guión bajo (_) a la secuencia alineada
            secuencia_alineada += "_"
    
    # Completar el resto de la secuencia2 con guiones bajos (_)
    secuencia_alineada += "_" * (len(secuencia2) - index_secuencia2)
    
    return secuencia_alineada

if __name__ == "__main__":
    # Leer las secuencias desde la entrada estándar
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")
    
    # Realizar el alineamiento
    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    
    # Imprimir el resultado
    print(secuencia_alineada)
  