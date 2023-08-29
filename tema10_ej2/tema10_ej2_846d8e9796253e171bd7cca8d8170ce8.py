#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    # Crear una matriz de distancias y llenarla con ceros
    matriz = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Llenar la primera fila y la primera columna con valores de 0 a len1 y len2 respectivamente
    for i in range(len1 + 1):
        matriz[i][0] = i
    for j in range(len2 + 1):
        matriz[0][j] = j

    # Calcular la distancia de edición entre las palabras
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(
                    matriz[i - 1][j] + 1,  # Eliminación
                    matriz[i][j - 1] + 1,  # Inserción
                    matriz[i - 1][j - 1] + 1  # Sustitución
                )

    # Obtener la distancia de edición entre las palabras
    distancia = matriz[len1][len2]

    # Determinar el resultado según la distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len1 < len2:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    else:
        return "0D"  # Palabras iguales

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
