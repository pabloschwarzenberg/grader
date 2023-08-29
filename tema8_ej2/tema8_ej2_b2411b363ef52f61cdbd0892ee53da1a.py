def buscarTodas(a,b):
    l=list(a)
    m=[]
    for i in range(0,len(l)):
        if l[i]==b:
          m.append(str(i))
        else:
          pass
    return " ".join(m)
    

           