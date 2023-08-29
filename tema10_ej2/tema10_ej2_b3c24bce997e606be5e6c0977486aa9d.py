#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):

    m = len(palabra1)
    n = len(palabra2)
    a = palabra1.upper()
    b = palabra2.upper()
    tabla = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        tabla[i][0] = i
    for j in range(n + 1):
        tabla[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                tabla[i][j] = tabla[i - 1][j - 1]
            else:
                tabla[i][j] = 1 + min(tabla[i - 1][j], tabla[i][j - 1], tabla[i - 1][j - 1])
    if tabla[-1][-1] > 1 :
        return "+1"
    elif tabla[-1][-1] == 1 :
        if m == n or a == b:
            return "1S"
        else:
            return "IB"
    elif tabla[-1][-1] == 0:
        return "0D"