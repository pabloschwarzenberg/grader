def buscarTodas(a,b):
    lista =[]
    l=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            s=l.join(lista)
        if(len(lista)==0):
          return "no existe"

    return s