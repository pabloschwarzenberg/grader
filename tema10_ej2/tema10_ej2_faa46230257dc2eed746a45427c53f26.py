#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    m = len(palabra1)
    n = len(palabra2)
    table = [[0] * (n+1) for k in range(m+1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table [0][j] = j

    for i in range(1, m+1):
        for j in range(1, n + 1):
            if palabra1[i-1] == palabra2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])

    return table[-1][-1]
           