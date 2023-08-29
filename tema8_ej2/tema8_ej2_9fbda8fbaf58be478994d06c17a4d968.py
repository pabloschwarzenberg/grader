def buscarTodas(Sub_a,Sub_b):

     Sub_m=[i for i,x in enumerate(Sub_a) if x==Sub_b]

     Sub_z=list(Sub_m)

     l=[]

     for i in Sub_z:

          l.append(str(i))

     h=" ".join(l)

     return h