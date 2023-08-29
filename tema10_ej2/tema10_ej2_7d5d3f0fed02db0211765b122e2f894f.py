def levenshtein(str1,str2):
    lista1 = []
    lista2 = []
    i = 0
    cont1 = 0
    for x in str1:
        lista1.append(x)
    for y in str2:
        lista2.append(y)
    while i < len(str1):
        if len(str1) != len(str2):
            break
        char1 = lista1[i]
        char2 = lista2[i]
        if char1 == char2:
            cont1 += 1
        i += 1
    if cont1 == len(str1) and cont1 == len(str2):
        return "0D"
    else:
        ver = len(str1) - len(str2)
        uver = True
        cont = 0
        sim = 0
        dif = 0
        while uver:
            if cont == len(lista1) or cont == len(lista2):
                uver = False
                break
            prim = lista1[cont]
            seg = lista2[cont]
            if prim == seg:
                sim += 1
            else:
                dif += 1
            cont += 1
        if sim - dif < 0:
            return "+1"
        if ver < 0:
            ver = ver * -1
            if ver == 1:
                return "IB"
            elif ver > 1:
                return "+1"
        elif ver == 0 or ver == 1:
            if ver == 0:
                return "1S"
            elif ver == 1:
                return "IB"
        elif ver > 1:
            return "+1"