def buscarTodas(a,b):
    lpalabra=[]
    for c,i in enumerate(a) :
        if (i == b):
            lpalabra.append(c)
    StrA = " ".join([str(_) for _ in lpalabra])
    return StrA
           