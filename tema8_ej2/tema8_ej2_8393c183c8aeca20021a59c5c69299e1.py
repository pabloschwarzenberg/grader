def buscarTodas(a,b):
    lista =[]
    agregar=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            l=agregar.join(lista)
        if(len(lista)==0):
          return "no existe"
    
    return l