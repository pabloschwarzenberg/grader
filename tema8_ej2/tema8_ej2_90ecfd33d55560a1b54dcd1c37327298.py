def buscarTodas(a,b):

     p=[i for i,x in enumerate(a) if x==b]

     y=list(p)

     l=[]

     for i in y:

          l.append(str(i))

     r=" ".join(l)

     return r