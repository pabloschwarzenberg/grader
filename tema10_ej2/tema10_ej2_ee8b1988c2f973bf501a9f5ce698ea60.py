def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"
    
    if m == n:
        if palabra1 == palabra2:
            return "0D"
        else:
            sustituciones = sum(1 for a, b in zip(palabra1, palabra2) if a != b)
            if sustituciones == 1:
                return "1S"
            else:
                return "+1"
    
    if m < n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    for i in range(n):
        if palabra1[i] != palabra2[i]:
            if palabra1[i+1:] == palabra2[i:]:
                return "IB"
            else:
                return "+1"

    return "IB"
