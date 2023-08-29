def buscarTodas(a,b):
     buscar = [i for i,o in enumerate(a) if o==b]
     buscar_2 = list(buscar)
     o = []
     for i in buscar:
          o.append(str(i))
     final = " ".join(o)
     return final