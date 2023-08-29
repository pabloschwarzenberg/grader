def buscarTodas(x,y):
    lista =[]
    s=" "
    for i in range(len(x)):
        if(x[i]==y):
            lista.append(str(i))
            l=s.join(lista)
        if(len(lista)==0):
          return "no existe"

    return l