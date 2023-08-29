def buscarTodas(a,b):
  string=[]
  pos=0
  for i in a:
    if  b in i:
      string.append(str(pos))
    pos+=1
    respuesta=" ".join(string)
  return respuesta
           