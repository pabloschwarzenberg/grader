def buscarTodas(a,b):
    Lista =[]
    v=" "
    for i in range(len(a)):
        if(a[i]==b):
            Lista.append(str(i))
            l=v.join(Lista)
        if(len(Lista)==0):
          return "NO EXISTE"
    
    return l  

           