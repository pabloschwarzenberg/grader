#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    
    # Crear la matriz de distancia y llenar la primera fila y columna
    distancia = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j
    
    # Calcular la distancia mínima
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(distancia[i - 1][j], distancia[i][j - 1], distancia[i - 1][j - 1]) + 1
    
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
    elif distancia[m][n] == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Distancia:", resultado)
