def buscarTodas(a,b):
    a = list(a)
    lv = []
    c = 0
    d = []
    for i in range(len(a)) :
        if a[i] != " " :
            lv += a[i]
        elif [i] == " " :
            for j in range(len(lv)) :
                if lv[j] == b :
                    c += 1
            d += list(str(c) + " ")
            continue
        elif i == len(a) - 1 :
            for j in range(len(lv)) :
                if lv[j] == b :
                    c += 1
            d += list(str(c) + " ")
            continue
    return ''.join(d)