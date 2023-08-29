def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    # Crear matriz de distancia
    distancia = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar primera fila y columna
    for i in range(len1 + 1):
        distancia[i][0] = i
    for j in range(len2 + 1):
        distancia[0][j] = j

    # Calcular distancia mínima
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(distancia[i - 1][j], distancia[i][j - 1], distancia[i - 1][j - 1]) + 1

    # Determinar resultado según distancia
    if distancia[len1][len2] > 1:
        return "+1"
    elif distancia[len1][len2] == 1:
        if len1 < len2:
            return "IB"
        elif len1 > len2:
            return "DB"
        else:
            return "1S"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
