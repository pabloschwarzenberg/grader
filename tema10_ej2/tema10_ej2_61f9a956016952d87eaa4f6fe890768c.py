def levenshtein(palabra1, palabra2):
    size_x = len(palabra1) + 1
    size_y = len(palabra2) + 1
    matrix = [[0 for _ in range(size_y)] for _ in range(size_x)]
    
    for x in range(size_x):
        matrix [x][0] = x
    for y in range(size_y):
        matrix [0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if palabra1[x-1] == palabra2[y-1]:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1],
                    matrix[x][y-1] + 1
                )
            else:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1] + 1,
                    matrix[x][y-1] + 1
                )

    distancia = matrix[size_x - 1][size_y - 1]
    
    if distancia == 0:
        return "0D"
    elif distancia == 1:
        if len(palabra1) == len(palabra2):
            return "1S"
        else:
            return "IB"
    else:
        return "+1"

if __name__=="__main__":
    print(levenshtein("gato", "gatito"))  # Debería imprimir "+1"
    print(levenshtein("hola", "ola"))  # Debería imprimir "IB"
    print(levenshtein("gallina", "gallina"))  # Debería imprimir "0D"
    print(levenshtein("caro", "cara"))  # Debería imprimir "1S"