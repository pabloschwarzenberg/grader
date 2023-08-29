def buscarTodas(a,b):
    x = 0
    listPos = []
    while x < len(a):
        posPalabra = x
        if a[x] == b:
            listPos = listPos + [str(x)]
        x += 1
    strPos = ' '.join(listPos)
    return strPos