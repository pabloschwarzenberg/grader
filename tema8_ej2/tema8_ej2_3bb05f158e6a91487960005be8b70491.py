def buscarTodas(a,b):
    li =[]
    agregar=" "
    for i in range(len(a)):
        if(a[i]==b):
            li.append(str(i))
            l=agregar.join(li)
        if(len(li)==0):
          return "no existe"
    
    return l