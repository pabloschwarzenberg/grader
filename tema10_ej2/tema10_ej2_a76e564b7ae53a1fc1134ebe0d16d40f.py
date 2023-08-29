def levenshtein(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    if abs(len1 - len2) > 1:
        return "+1"
    
    if len1 == len2:
        diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
        if diff_count == 0:
            return "0D"
        elif diff_count == 1:
            return "1S"
        else:
            return "+1"

    if len1 > len2:
        word1, word2 = word2, word1
        len1, len2 = len2, len1

    i = j = 0
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

    return "IB"

if __name__ == "__main__":
    word1 = "gato"
    word2 = "gatito"
    result = levenshtein(word1, word2)
    print(result)
          