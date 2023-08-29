def buscarTodas(a,b):
    res = []
    for i in range(len(a)):
        if a[i] == b:
            res.append(str(i))
    return ' '.join(res)