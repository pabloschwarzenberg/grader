def buscarTodas(a,b):
    i=0
    L=[]
    while i<len(a):
        if a[i]==b:
            L.append(str(i))
            i+=1
        else:
            i+=1

    a=" ".join(L)
    return a
      


           