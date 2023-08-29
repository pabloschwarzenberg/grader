def buscarTodas(a,b):
     p=[i for i,x in enumerate(a) if x==b]
     g=list(p)
     l=[]
     for i in g:
          l.append(str(i))
     w=" ".join(l)
     return w

           