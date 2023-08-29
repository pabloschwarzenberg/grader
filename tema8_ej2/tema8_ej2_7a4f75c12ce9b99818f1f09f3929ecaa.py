def buscarTodas(a,b):
    lista = []
    c = ""
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
    for x in lista:
      if x == lista[-1]:
        c = c + str(x)
      else:
        c = c + str(x) + " "
    return c