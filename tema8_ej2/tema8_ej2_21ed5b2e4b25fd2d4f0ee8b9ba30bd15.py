def buscarTodas(a,b):

     u=[i for i,x in enumerate(a) if x==b]

     j=list(u)

     n=[]

     for i in j:

          n.append(str(i))

     w=" ".join(n)

     return w
           