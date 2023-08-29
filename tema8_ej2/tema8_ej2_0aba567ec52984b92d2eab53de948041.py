def buscarTodas(a,b):
    listado =[]
    s=" "
    for i in range(len(a)):
        if(a[i]==b):
            listado.append(str(i))
            l=s.join(listado)
        if(len(listado)==0):
          return "no existe"
    return l 