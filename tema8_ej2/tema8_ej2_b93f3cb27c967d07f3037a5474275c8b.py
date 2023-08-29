#buscarTodas("tres tristes tigres","t")




def buscarTodas(a,b):
    m = [i for i,x in enumerate(a) if x == b]
    z= list(m)
    I=[]
    for i in z:
        I.append(str(i))
    w = " ".join(I)
    return print("%s" % w )
buscarTodas("tres tristes tigres" , "t")