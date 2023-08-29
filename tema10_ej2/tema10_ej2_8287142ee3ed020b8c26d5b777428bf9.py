def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if palabra1 == palabra2:
        return "0D"

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    if dp[len1][len2] == 1:
        if len1 == len2:
            return "1S"
        else:
            return "IB"
    else:
        return "+1"


# Ejemplo de uso
palabra1 = "gato"
palabra2 = "gatito"
resultado = levenshtein(palabra1, palabra2)
print(resultado)  # +1

palabra1 = "caro"
palabra2 = "cara"
resultado = levenshtein(palabra1, palabra2)
print(resultado)  # 1S

palabra1 = "Limon"
palabra2 = "limon"
resultado = levenshtein(palabra1, palabra2)
print(resultado)  # 1S

palabra1 = "jarron"
palabra2 = "melon"
resultado = levenshtein(palabra1, palabra2)
print(resultado)  # +1

palabra1 = "jaron"
palabra2 = "jarron"
resultado = levenshtein(palabra1, palabra2)
print(resultado)  # IB
