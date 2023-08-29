def levenshtein(palabra1,palabra2):
    if not palabra1:
        return len(palabra2)
    if not palabra2:
        return len(palabra1)

    return min(levenshtein(palabra1[1:], palabra2[1:])+(palabra1[0] != palabra2[0]),
               levenshtein(palabra1[1:], palabra2)+1,
               levenshtein(palabra1, palabra2[1:])+1)

    
           