def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    elif abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"
    else:
        if len(palabra1) < len(palabra2):
            palabra1, palabra2 = palabra2, palabra1
        m = len(palabra1)
        n = len(palabra2)
        dp = [[0 for x in range(n+1)] for x in range(2)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i%2][j] = j
                elif j == 0:
                    dp[i%2][j] = i
                elif palabra1[i-1] == palabra2[j-1]:
                    dp[i%2][j] = dp[(i-1)%2][j-1]
                else:
                    dp[i%2][j] = 1 + min(dp[(i-1)%2][j], dp[i%2][j-1], dp[(i-1)%2][j-1])
        if dp[m%2][n] == 1:
            if len(palabra1) == len(palabra2):
                return "1S"
            else:
                return "IB"
        elif dp[m%2][n] == 2:
            return "1S"
        else:
            return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)