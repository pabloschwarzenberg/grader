def buscarTodas(a,b):
     r=[i for i,x in enumerate(a) if x==b]
     w=list(r)
     p=[]
     for i in w:
          p.append(str(i))
     x=" ".join(p)
     return x
