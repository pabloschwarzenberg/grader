# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
# insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    # Crear una matriz de distancias
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Inicializar la primera fila y la primera columna
    for i in range(len1 + 1):
        distances[i][0] = i
    for j in range(len2 + 1):
        distances[0][j] = j

    # Calcular las distancias
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                insert_cost = distances[i][j - 1] + 1
                delete_cost = distances[i - 1][j] + 1
                replace_cost = distances[i - 1][j - 1] + 1
                distances[i][j] = min(insert_cost, delete_cost, replace_cost)

    # Obtener la distancia final
    final_distance = distances[len1][len2]

    # Determinar el resultado según la distancia
    if final_distance > 1:
        return "+1"
    elif final_distance == 1:
        if len1 > len2 or len1 < len2:
            return "IB"
        else:
            return "1S"
    elif final_distance == 0:
        return "0D"