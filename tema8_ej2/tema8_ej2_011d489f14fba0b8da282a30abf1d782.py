def buscarTodas(a,b):

     k=[i for i,x in enumerate(a) if x==b]

     v=list(k)

     p=[]

     for i in v:

          p.append(str(i))

     w=" ".join(p)

     return w
           