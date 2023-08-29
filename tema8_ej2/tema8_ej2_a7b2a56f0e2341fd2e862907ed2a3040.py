def buscarTodas(a,b):
 d=list(a)
 z=[]
 for c in d:
     if c==b:
         x=(d.index(b))
         rep=str(d.index(b))
         d[x]=(".")
         z.append(rep)
         y=" ".join(z)
 return (y)
         
if __name__ == "__main__":
    pass
           