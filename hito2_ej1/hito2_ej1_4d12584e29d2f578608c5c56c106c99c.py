# Definimos la función que alinea dos secuencias de ADN
def alinear_secuencias(secuencia_1, secuencia_2):
    # Convertimos las secuencias en listas para poder modificarlas
    lista_secuencia_1 = list(secuencia_1)
    lista_secuencia_2 = list(secuencia_2)
    # Inicializamos el índice para recorrer la segunda secuencia
    indice_2 = 0
    # Recorremos la primera secuencia
    for i in range(len(lista_secuencia_1)):
        # Si el caracter de la primera secuencia es igual al de la segunda, avanzamos en ambos índices
        if lista_secuencia_1[i] == lista_secuencia_2[indice_2]:
            indice_2 += 1
        # Si no, insertamos un guión bajo en la segunda secuencia para alinearla con la primera
        else:
            lista_secuencia_2.insert(indice_2, "_")
            indice_2 += 1 # Agregamos el incremento del índice para que no se quede en el mismo lugar
    # Convertimos la segunda secuencia de nuevo en un string y la retornamos dentro de una lista
    secuencia_alineada = "".join(lista_secuencia_2)
    return [secuencia_alineada]

# Ejemplo de uso
secuencia_1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia_2 = "TGACGTTCAGTAGTCGATT"
secuencia_alineada = alinear_secuencias(secuencia_1, secuencia_2)
print(secuencia_alineada) # Debería imprimir: ['___TG_______A__C_G__TT_C_AGTAGTCGATT']