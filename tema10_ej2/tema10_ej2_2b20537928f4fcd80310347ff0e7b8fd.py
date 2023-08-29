def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    
    if abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"
    
    if len(palabra1) == len(palabra2):
        diferencias = 0
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                diferencias += 1
        if diferencias == 1:
            return "1S"
        else:
            return "+1"
    if abs(len(palabra1) - len(palabra2)) == 1:
        if len(palabra1) > len(palabra2):
            palabra1, palabra2 = palabra2, palabra1
        
        i = 0 
        j = 0 
        diferencias = 0
        while i < len(palabra1) and j < len(palabra2):
            if palabra1[i] == palabra2[j]:
                i += 1
                j += 1
            else:
                j += 1
                diferencias += 1
        
        if diferencias == 1:
            return "IB"
        else:
            return "+1"
