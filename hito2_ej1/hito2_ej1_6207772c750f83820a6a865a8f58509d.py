def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice = 0
    
    # Recorrer la primera secuencia
    for i in range(len(secuencia1)):
        if indice < len(secuencia2) and secuencia1[i] == secuencia2[indice]:
            alineacion += secuencia2[indice]
            indice += 1
        else:
            alineacion += "_"
    
    # Agregar los caracteres restantes de la segunda secuencia
    alineacion += secuencia2[indice:]
    
    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")
    
    resultado = alinear_secuencias(secuencia1, secuencia2)
    
    print(resultado)