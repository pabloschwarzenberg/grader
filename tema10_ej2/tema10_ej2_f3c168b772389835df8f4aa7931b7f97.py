#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: una de las palabras es vacía
    if m == 0 or n == 0:
        return "IB" if abs(m - n) == 1 else "+1"

    # Crear una matriz para almacenar los cálculos intermedios
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Determinar el resultado según la distancia calculada
    distancia = dp[m][n]
    if distancia == 0:
        return "0D"
    elif distancia > 1:
        return "+1"
    elif abs(m - n) == 1:
        return "IB"
    else:
        return "1S"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia Levenshtein:", resultado)

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia Levenshtein:", resultado)

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia Levenshtein:", resultado)

    palabra1 = "caro"
    palabra2 = "cara"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia Levenshtein:", resultado)
