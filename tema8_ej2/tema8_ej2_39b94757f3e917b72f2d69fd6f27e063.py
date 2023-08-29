def buscarTodas(a,b):
    LIST =[]
    vrbl =" "
    for i in range(len(a)):
        if(a[i]==b):
            LIST.append(str(i))
            l=vrbl.join(LIST)
        if(len(LIST)==0):
          return "no existe"
    
    return l

           