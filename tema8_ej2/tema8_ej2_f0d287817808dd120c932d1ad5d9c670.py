def buscarTodas(a,b):

     n=[i for i,y in enumerate(a) if y == b]

     t=list(n)

     d=[]

     for i in t:

          d.append(str(i))

     p=" ".join(d)

     return p
     

