def buscarTodas(a, b):
    l  = list(a)
    i = ""
    for x in range(0,len(a)):
        if l[x] == b:
            i += str(x)+" "
    i = i.strip()
    return i
