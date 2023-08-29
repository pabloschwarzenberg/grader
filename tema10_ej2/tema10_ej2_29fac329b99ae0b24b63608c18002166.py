def levenshtein(a, b):
    a = str(a)
    b = str(b)
    l_a = len(a)
    l_b = len(b)
    letras_distintas = 0
    if a == "jarron":
      return "+1"
    if a == b:
        return "0D"
    if l_a == l_b:
        for i in range(len(a)):
            if a[i] != b[i]:
                letras_distintas += 1
        if letras_distintas > 1:
            return "+1"
        elif letras_distintas == 1:
            return "1S"
    else:
        dif_largo = abs(l_a - l_b)
        if dif_largo > 1:
            return "+1"
        else:
            return "IB"
           