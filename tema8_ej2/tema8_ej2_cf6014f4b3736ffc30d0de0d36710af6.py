def buscarTodas(a,b):
  lista1=list(a)
  cont=0
  lista2=[]
  while len (lista1) > cont :
   if lista1 [cont] == b :
            lista2.append (str(cont))
            lista2.append (" ")
   cont=cont +1 
  lista2.pop (len(lista2)-1)
  lista2="".join(lista2)
  return lista2