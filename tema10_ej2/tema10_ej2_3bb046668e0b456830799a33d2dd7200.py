def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de distancia con m+1 filas y n+1 columnas
    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz de distancia
    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j

    # Calcular la distancia de edición entre las palabras
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = 1 + min(
                    distancia[i - 1][j],       # Eliminación
                    distancia[i][j - 1],       # Inserción
                    distancia[i - 1][j - 1]    # Sustitución
                )

    # Determinar el tipo de distancia
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
      print(f"Distancia: {resultado}")