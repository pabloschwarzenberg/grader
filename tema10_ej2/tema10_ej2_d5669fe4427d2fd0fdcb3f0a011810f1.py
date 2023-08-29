def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"

    len1 = len(word1)
    len2 = len(word2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 == len2:
        diff_count = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)
        if diff_count == 1:
            return "1S"

    if len1 > len2:
        word1, word2 = word2, word1
        len1, len2 = len2, len1

    i = 0
    j = 0
    diff_count = 0

    while i < len1 and j < len2:
        if word1[i] != word2[j]:
            diff_count += 1
            if diff_count > 1:
                return "+1"
            if len1 != len2:
                i -= 1
        i += 1
        j += 1

    return "IB" if diff_count == 1 else "+1"


if __name__ == "__main__":
    # Pruebas de ejemplo
    print(levenshtein("gato", "gatito"))  # Debería imprimir: +1
    print(levenshtein("hola", "ola"))  # Debería imprimir: IB
    print(levenshtein("gallina", "gallina"))  # Debería imprimir: 0D
    print(levenshtein("caro", "cara"))  # Debería imprimir: 1S
