def buscarTodas(a,b):
     r=[i for i,x in enumerate(a) if x==b]
     d=list(r)
     f=[]
     for i in d:
          f.append(str(i))
     w=" ".join(f)
     return w
