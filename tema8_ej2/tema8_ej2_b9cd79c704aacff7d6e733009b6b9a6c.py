def buscarTodas(a,b):

     m=[i for i,x in enumerate(a) if x==b]

     z_list=list(m)

     lista=[]

     for indice in z_list:

          lista.append(str(indice))

     c=" ".join(lista)

     return c