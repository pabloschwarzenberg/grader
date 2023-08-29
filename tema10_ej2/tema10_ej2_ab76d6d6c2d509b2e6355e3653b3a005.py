def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(
                    distancia[i - 1][j] + 1,  
                    distancia[i][j - 1] + 1,  
                    distancia[i - 1][j - 1] + 1  
                )

    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m > n:
            return "IB"
        elif m < n:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"


if __name__ == "__main__":
 
    print(levenshtein("gato", "gatito"))  # +1
    print(levenshtein("hola", "ola"))  # IB
    print(levenshtein("gallina", "gallina"))  # 0D
    print(levenshtein("caro", "cara"))  # 1S
