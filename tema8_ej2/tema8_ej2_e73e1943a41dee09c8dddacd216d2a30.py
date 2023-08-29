def buscarTodas(a,b):
     c=[i for i,x in enumerate(a) if x==b]
     d=list(c)
     e=[]
     for i in d:
          e.append(str(i))
     f=" ".join(e)
     return f