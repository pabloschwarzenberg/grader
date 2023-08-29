def buscarTodas(j,a):

     p=[i for i,x in enumerate(j) if x==a]

     q=list(p)

     l=[]

     for i in q:

          l.append(str(i))

     e=" ".join(l)

     return e