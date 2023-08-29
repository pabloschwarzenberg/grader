def levenshtein(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    
    for i in range(len1 + 1):
        distances[i][0] = i
    for j in range(len2 + 1):
        distances[0][j] = j

    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = 1 + min(distances[i - 1][j], distances[i][j - 1], distances[i - 1][j - 1])

    
    distance = distances[len1][len2]
    if distance > 1:
        return "+1"
    elif distance == 1:
        if len1 > len2:
            return "IB"
        elif len2 > len1:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
if __name__ == "__main__":
    word1 = "gato"
    word2 = "gatito"
    result = levenshtein(word1, word2)
    print("The result is:" ,result)