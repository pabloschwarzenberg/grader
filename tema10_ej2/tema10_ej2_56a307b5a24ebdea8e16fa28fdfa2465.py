#La funciÃ³n debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def main():
    mensaje = input("Ingrese mensaje: ")
    print(decodificar(mensaje))
def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"
    m, n = len(word1), len(word2)
    if abs(m - n) > 1:
        return "+1"
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    if dp[m][n] > 1:
        return "+1"
    elif dp[m][n] == 1:
        if m < n:
            return "IB"
        else:
            return "1S"
    elif m == n:
        return "0D"
    elif m < n:
        return "IB"
    else:
        return "IB"

print(levenshtein("gato", "gatito"))  # +1
print(levenshtein("hola", "ola"))  # IB
print(levenshtein("gallina", "gallina"))  # 0D
print(levenshtein("caro", "cara"))  # 1S
print(levenshtein("Limon", "limon"))  # 1S
print(levenshtein("jaron", "jarron"))  # IB
def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    if secuencia.isalpha() and all(letra in "ACTG" for letra in secuencia):
        return "secuencia correcta"
    return "secuencia incorrecta"  