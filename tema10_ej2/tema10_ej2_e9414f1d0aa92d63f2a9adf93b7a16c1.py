#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz de tamaño (m+1) x (n+1) e inicializarla con ceros
    matriz = [[0] * (n+1) for _ in range(m+1)]

    # Inicializar la primera columna de la matriz
    for i in range(m+1):
        matriz[i][0] = i

    # Inicializar la primera fila de la matriz
    for j in range(n+1):
        matriz[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m+1):
        for j in range(1, n+1):
            if palabra1[i-1] == palabra2[j-1]:
                matriz[i][j] = matriz[i-1][j-1]
            else:
                matriz[i][j] = min(matriz[i-1][j-1] + 1, matriz[i][j-1] + 1, matriz[i-1][j] + 1)

    # Obtener la distancia Levenshtein final
    distancia = matriz[m][n]

    # Determinar el resultado según la distancia
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if m < n else "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
