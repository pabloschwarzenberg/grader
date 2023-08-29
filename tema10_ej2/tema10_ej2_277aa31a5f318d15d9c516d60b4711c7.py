#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    if m == 0 or n == 0:
        if abs(m - n) == 1:
            return "IB"
        else:
            return "+1"
    distancias = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        distancias[i][0] = i
    for j in range(n+1):
        distancias[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if palabra1[i-1] == palabra2[j-1]:
                distancias[i][j] = distancias[i-1][j-1]
            else:
                distancias[i][j] = min(distancias[i-1][j], distancias[i][j-1], distancias[i-1][j-1]) + 1
    distancia = distancias[m][n]
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
           