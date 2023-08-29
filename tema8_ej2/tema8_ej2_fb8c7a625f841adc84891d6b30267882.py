def buscarTodas(a,b):
    m =[idx for idx, x in enumerate(a) if x==b]
    c=m[len(m)-1]
    z = ""
    for i in m:
        if i !=c:
            z = z + str(i) + " "
        else:
            z = z + str(i)
    return z