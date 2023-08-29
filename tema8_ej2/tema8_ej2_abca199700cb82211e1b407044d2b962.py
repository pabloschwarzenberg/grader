def buscarTodas(a,b):
     t=[i for i,x in enumerate(a) if x==b]

     v=list(t)

     q=[]

     for i in v:

          q.append(str(i))

     x=" ".join(q)

     return x
           