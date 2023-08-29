def buscarTodas(a,b):
    x=list(a)    
    numero=""
    for i in range(0,len(x)):
      if x[i]==b:
          numero+=str(i)+" "
    q=list(numero)
    q.pop(len(numero)-1)
    ahora="".join(q)
    return ahora




 