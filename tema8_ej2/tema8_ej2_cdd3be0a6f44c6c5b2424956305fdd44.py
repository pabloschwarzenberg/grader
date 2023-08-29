def buscarTodas(a,b):
    l = []
    cd = 0
    r = ""
    for j in range(len(a)):
        l.append("_")

    for i in a:
        if i == b:
            r += str(cd)+" "
        cd += 1
    return r
