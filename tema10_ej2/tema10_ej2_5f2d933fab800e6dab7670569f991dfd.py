def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Creamos una matriz de distancias con m+1 filas y n+1 columnas
    distancias = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera fila y columna de la matriz de distancias
    for i in range(m + 1):
        distancias[i][0] = i
    for j in range(n + 1):
        distancias[0][j] = j

    # Calculamos las distancias para el resto de las celdas de la matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancias[i][j] = distancias[i - 1][j - 1]
            else:
                distancias[i][j] = min(
                    distancias[i - 1][j] + 1,  # Eliminación
                    distancias[i][j - 1] + 1,  # Inserción
                    distancias[i - 1][j - 1] + 1  # Sustitución
                )

    # Obtenemos la distancia final
    distancia = distancias[m][n]

    # Determinamos el tipo de transformación requerida según la distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m != n:
            return "IB"  # Insertar o borrar
        else:
            return "1S"  # Sustituir
    else:
        return "0D"  # Igual

if __name__ == "__main__":
    # Ejemplos de uso
    print(levenshtein("caro", "cara"))  # 1S
    print(levenshtein("Limon", "limon"))  # 1S
