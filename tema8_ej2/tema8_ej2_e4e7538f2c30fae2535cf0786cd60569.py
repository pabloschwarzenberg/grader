def buscarTodas(a,b):
  resultado=""
  indice=0
  while indice != -1:
    if(a.find(b, indice) != -1):
      resultado+=' '+str(a.find(b, indice))
    indice=a.find(b, indice)
    if(indice == 0):
      indice+=1
    else:
      if(indice != -1):
        indice+=1

  return resultado


           