def buscarTodas(j,k):

     n=[i for i,y in enumerate(j) if y==k]

     f=list(n)

     long=[]

     for i in f:

          long.append(str(i))

     e=" ".join(long)

     return e
