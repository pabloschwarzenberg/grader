def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Palabras iguales

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"  # Distancia mayor a 1

    # Crear matriz de distancias
    matriz = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        matriz[i][0] = i

    for j in range(len2 + 1):
        matriz[0][j] = j

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

    distancia = matriz[len1][len2]

    if distancia > 1:
        return "+1"  # Distancia mayor a 1
    elif len1 > len2:
        return "IB"  # Insertar o borrar
    elif len1 < len2:
        return "IB"  # Insertar o borrar
    else:
        return "1S"  # Sustitución

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("El resultado es:", resultado)

           