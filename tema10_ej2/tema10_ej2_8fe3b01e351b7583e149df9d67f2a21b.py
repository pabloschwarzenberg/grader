#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(word1,word2):
    m = len(word1)
    n = len(word2)
    tab = [[0] * (n+1) for _ in range(m +1)]

    for i in range(m + 1):
        tab[i][0] = i
    for j in range(n + 1):
        tab[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j -1]:
                tab[i][j] = tab[i - 1][j - 1]
            else:
                tab[i][j] = 1 + min(tab[i - 1][j], tab[i][j - 1], tab[i - 1][j - 1])

    return tab[-1][-1]