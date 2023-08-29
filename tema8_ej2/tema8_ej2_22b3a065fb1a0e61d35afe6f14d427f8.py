def buscarTodas(a,b):

     frases=[i for i,x in enumerate(a) if x==b]

     z=list(frases)

     largo=[]

     for i in z:

          largo.append(str(i))

     resultado=" ".join(largo)

     return resultado