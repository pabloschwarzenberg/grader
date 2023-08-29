#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(word1, word2):
    m, n = len(word1), len(word2)
    if abs(m - n) > 1:
        return "+1"
    
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    distance = dp[m][n]
    if distance > 1:
        return "+1"
    elif distance == 1:
        return "IB" if m < n else "1S"
    else:
        return "0D"


if __name__ == "__main__":
    word_pairs = [("gato", "gatito"), ("hola", "ola"), ("gallina", "gallina"), ("caro", "cara")]
    
    for word1, word2 in word_pairs:
        distance = levenshtein(word1, word2)
        print("Palabras:", word1 - word2)
        print("Resultado:", distance)
        print()
