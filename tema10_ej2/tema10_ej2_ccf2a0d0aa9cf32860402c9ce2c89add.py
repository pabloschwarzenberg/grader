def levenshtein(word1, word2):
    len1, len2 = len(word1), len(word2)

    if len1 == len2:
        if word1 == word2:
            return "0D"  # Mismo tamaño y son iguales
        else:
            return "+1"  # Mismo tamaño pero diferentes

    if abs(len1 - len2) > 1:
        return "+1"  # Distancia mayor a 1

    if len1 > len2:
        word1, word2 = word2, word1
        len1, len2 = len2, len1

    i, j, edit_distance = 0, 0, 0
    is_insert_delete = False

    while i < len1 and j < len2:
        if word1[i] != word2[j]:
            if is_insert_delete:
                return "+1"
            else:
                edit_distance += 1
                if len1 < len2:
                    i -= 1
                elif len1 > len2:
                    j -= 1
                is_insert_delete = True

        i += 1
        j += 1

    edit_distance += len2 - j
    if edit_distance == 1:
        return "IB" if is_insert_delete else "1S"
    elif edit_distance == 0:
        return "0D"
    else:
        return "+1"


if __name__ == "__main__":
    word1 = "gato"
    word2 = "gatito"
    result = levenshtein(word1, word2)
    print(result)
