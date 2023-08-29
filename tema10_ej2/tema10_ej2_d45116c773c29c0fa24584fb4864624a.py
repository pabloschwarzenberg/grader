#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
##DISTANCIA LEVENSHTEIN
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear una matriz para almacenar los resultados parciales
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar la primera fila y la primera columna de la matriz
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

    # Determinar el resultado según la distancia Levenshtein
    distancia = matriz[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
       