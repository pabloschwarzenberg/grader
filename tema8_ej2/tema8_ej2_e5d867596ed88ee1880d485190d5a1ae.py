def buscarTodas(a,b):

     op_1=[i for i,z in enumerate(a) if z==b]

     op_2=list(op_1)

     op_3=[]

     for i in op_2:

          op_3.append(str(i))

     op_4=" ".join(op_3)

     return op_4