def buscarTodas(a,b):
 
     m=[i for i,x in enumerate(a) if x==b]
     
     w=list(m)
     
     l=[]
     
     for i in w:
     
          l.append(str(i))
          
     z=" ".join(l)
     
     return z