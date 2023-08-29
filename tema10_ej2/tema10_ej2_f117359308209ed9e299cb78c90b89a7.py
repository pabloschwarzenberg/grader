def levenshtein(palabra1, palabra2):
    
    # Caso base: ambas palabras son iguales
    if palabra1 == palabra2:
        return "0D"
    
    # Cálculo de la matriz de distancias
    m = len(palabra1)
    n = len(palabra2)
    matriz = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        matriz[i][0] = i
    for j in range(1, n + 1):
        matriz[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                coste = 0
            else:
                coste = 1
            matriz[i][j] = min(matriz[i - 1][j] + 1,        # Borrar
                               matriz[i][j - 1] + 1,        # Insertar
                               matriz[i - 1][j - 1] + coste # Sustituir
                              )
    
    # Elección de la salida según la distancia resultante
    distancia = matriz[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        elif n > m:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"


if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    print(levenshtein(palabra1, palabra2)) # debe imprimir "+1"

    palabra1 = "hola"
    palabra2 = "ola"
    print(levenshtein(palabra1, palabra2)) # debe imprimir "IB"

    palabra1 = "gallina"
    palabra2 = "gallina"
    print(levenshtein(palabra1, palabra2)) # debe imprimir "
