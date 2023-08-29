def buscarTodas(a,b):
    list = []
    c = ("")
    for i in range(len(a)):
        if(a[i]==b):
            list.append(i)
    if(len(list)==0):
        return "no existe"
    for d in list:
      if d==list[-1]:
        c=c+str(d)
      else:
        c=c+str(d)+" "
    return c