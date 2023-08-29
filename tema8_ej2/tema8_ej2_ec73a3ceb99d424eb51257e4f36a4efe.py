def buscarTodas(a,b):
    lis =[]
    s=" "
    for i in range(len(a)):
        if(a[i]==b):
            lis.append(str(i))
            l=s.join(lis)
        if(len(lis)==0):
          return "no existe"
    
    return l  