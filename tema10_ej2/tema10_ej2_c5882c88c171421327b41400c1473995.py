def levenshtein(str1, str2):
    final = ""
    d = dict()
    for i in range(len(str1) + 1):
        d[i] = dict()
        d[i][0] = i
    for i in range(len(str2) + 1):
        d[0][i] = i
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + (not str1[i - 1] == str2[j - 1]))

    res = (d[len(str1)][len(str2)])

    if res > 1:
        print("soy mayor a 1")
        final = "+1"
        print(final)
    elif res == 0:
        print("soy 0")
        final = "0D"
        print(final)
    elif 1 == 1 and len(str1) == len(str2):
        print("soy 1")
        final = "1S"
        print("soy el print final",final)
    else:
        final = "IB"
        print("soy el final,", final)

    return final

if __name__ == "__main__":
    levenshtein("gato", "gatito")
