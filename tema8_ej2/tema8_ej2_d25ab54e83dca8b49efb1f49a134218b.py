def buscarTodas(x,y):

     a=[i for i,x in enumerate(x) if x==y]

     w=list(a)

     l=[]

     for i in w:

          l.append(str(i))

     z=" ".join(l)

     return z
