def buscarTodas(a,b):
    lista =[]
    S=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            l=S.join(lista)
        if(len(lista)==0):
          return "no existe"
    
    return l  