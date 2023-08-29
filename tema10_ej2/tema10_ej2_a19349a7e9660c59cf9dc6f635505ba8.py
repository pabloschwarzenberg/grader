def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)

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
        if m == n:
            return "1S"
        else:
            return "IB"
    else:
        return "0D"

if __name__ == "__main__":
    word1 = input("Ingrese la primera palabra: ")
    word2 = input("Ingrese la segunda palabra: ")
    result = levenshtein(word1, word2)
    print(result)
