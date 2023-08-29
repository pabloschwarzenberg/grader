#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
    pass

def levenshtein(word1, word2):
    m, n = len(word1), len(word2)

    # Caso base: si una de las palabras es vacía, la distancia es la longitud de la otra palabra
    if m == 0:
        return n
    if n == 0:
        return m

    # Creamos una matriz de tamaño (m+1)x(n+1) para almacenar los cálculos intermedios
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializamos la primera columna de la matriz
    for i in range(m + 1):
        dp[i][0] = i

    # Inicializamos la primera fila de la matriz
    for j in range(n + 1):
        dp[0][j] = j

    # Calculamos la distancia de edición para cada subproblema
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Si los caracteres son iguales, no hay costo adicional
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Si los caracteres son diferentes, consideramos todas las operaciones posibles
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # Obtenemos la distancia de edición entre las palabras
    distance = dp[m][n]

    # Determinamos el resultado según la distancia obtenida
    if distance > 1:
        return "+1"
    elif distance == 1:
        # Comprobamos si la distancia de edición es debido a una inserción o eliminación
        if m > n or n > m:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
