def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: si alguna de las palabras es vacía, la distancia es la longitud de la otra palabra
    if m == 0:
        return n
    if n == 0:
        return m

    # Creamos una matriz para almacenar los cálculos intermedios
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calculamos la distancia de Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    # Obtenemos la distancia final
    distancia = matriz[m][n]

    # Determinamos el resultado según la distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"


if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

    palabra1 = "caro"
    palabra2 = "cara"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
