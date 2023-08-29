def buscarTodas(a,b):
    p=[]
    for i in range (len(a)):
        if b == a[i]:
            p.append(i)

    Strp = " ".join([str(_) for _ in p])
    
    return Strp

           