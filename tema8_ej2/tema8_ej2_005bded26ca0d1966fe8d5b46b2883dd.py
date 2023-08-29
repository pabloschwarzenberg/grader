def buscarTodas(a,b):
    lista =[]
    s=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            l=s.join(lista)
        if(len(lista)==0):
          return "no existe"
    return l  