def buscarTodas(a,b):
     n = [i for i,x in enumerate(a) if x==b]
     y = list(n)
     l = []
     for i in y:
          l.append(str(i))
     v = " ".join(l)
     return v