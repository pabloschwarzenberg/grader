def buscarTodas(a,b):
     lista1=[i for i,x in enumerate(a) if x==b]
     z=list(lista1)
     lista2=[]
     for i in z:
          lista2.append(str(i))
     union=" ".join(lista2)

     return union