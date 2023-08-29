def buscarTodas(a,b):
    posiciones=""
    n=0
    for i in a:
        if i==b:
            if posiciones == "":
                nstr=str(n)
                posiciones+=nstr
                n += 1
            else:
                posiciones += ""
                nstr=str(n)
                posiciones += nstr
                n += 1
        else:
            n += 1
    return (posiciones,n)