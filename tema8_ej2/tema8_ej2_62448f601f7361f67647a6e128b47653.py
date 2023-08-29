def buscarTodas(a,b):

     z=[i for i,x in enumerate(a) if x==b]

     b=list(z)

     l=[]

     for i in b:

          l.append(str(i))

     r=" ".join(l)

     return r