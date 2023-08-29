def alinear_secuencias(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    i = n
    j = m
    resultado = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            resultado = s2[j - 1] + resultado
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            resultado = "_" + resultado
            i -= 1
        else:
            resultado = s2[j - 1] + resultado
            j -= 1

    while i > 0:
        resultado = "_" + resultado
        i -= 1

    return resultado

s1 = input("Ingresa el primer string: ")
s2 = input("Ingresa el segundo string: ")
s2_alineado = alinear_secuencias(s1, s2)
print(s2_alineado)
s1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
s2 = "TGACGTTCAGTAGTCGATT"
s2_alineado = alinear_secuencias(s1, s2)
print(s2_alineado)

