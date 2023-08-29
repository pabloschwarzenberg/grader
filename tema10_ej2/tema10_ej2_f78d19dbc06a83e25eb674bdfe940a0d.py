def levenshtein(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    # Crear una matriz de (len1 + 1) x (len2 + 1) para almacenar los cálculos intermedios
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(len1 + 1):
        matrix[i][0] = i
    for j in range(len2 + 1):
        matrix[0][j] = j

    # Calcular la distancia de Levenshtein
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,  # Eliminación
                    matrix[i][j - 1] + 1,  # Inserción
                    matrix[i - 1][j - 1] + 1  # Sustitución
                )

    # Obtener la distancia de Levenshtein final
    distance = matrix[len1][len2]

    # Determinar el tipo de distancia y retornar el resultado correspondiente
    if distance > 1:
        return "+1"
    elif distance == 1:
        if len1 > len2:
            return "IB"
        elif len1 < len2:
            return "IB"
        else:
            return "1S"
    elif distance == 0:
        return "0D"

if __name__ == "__main__":
    word1 = input("Ingrese la primera palabra: ")
    word2 = input("Ingrese la segunda palabra: ")

    result = levenshtein(word1, word2)
    print("Resultado:", result)
 