def buscarTodas(a,b):
    m=[i for i, x in enumerate(a) if x==b]
    z=list(m)
    l=[]
    for i in z:
        l.append(str(i))
    return print("%s" % l)
    
buscarTodas("tres tristes tigres","t")