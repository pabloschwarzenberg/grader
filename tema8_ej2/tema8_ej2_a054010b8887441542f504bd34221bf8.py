def buscarTodas(a,b):

     l=[i for i,x in enumerate(a) if x==b]

     v=list(l)

     t=[]

     for i in v:

          t.append(str(i))

     j=" ".join(t)
   

     return j

           