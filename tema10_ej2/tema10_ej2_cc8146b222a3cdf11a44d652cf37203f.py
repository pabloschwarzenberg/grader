def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"

    len1 = len(word1)
    len2 = len(word2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 == len2:
        count = 0
        for i in range(len1):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return "1S"

    if abs(len1 - len2) == 1:
        if len1 < len2:
            short_word, long_word = word1, word2
        else:
            short_word, long_word = word2, word1

        i = j = count = 0
        while i < len(short_word) and j < len(long_word):
            if short_word[i] != long_word[j]:
                count += 1
                if len1 < len2:
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j += 1

        if count == 1:
            return "IB"

    return "+1"
