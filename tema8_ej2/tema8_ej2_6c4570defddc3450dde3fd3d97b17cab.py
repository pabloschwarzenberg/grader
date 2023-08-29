def buscarTodas(a,b):
     f=[i for i,x in enumerate(a) if x==b]
     w=list(f)
     l=[]
     for i in w:
          l.append(str(i))
     r=" ".join(l)
     return r           