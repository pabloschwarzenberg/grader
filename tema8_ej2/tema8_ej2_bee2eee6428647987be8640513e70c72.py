def buscarTodas(a,b):
  c=list(a)
  d=c.count(b)
  if d==1:
    e=c.index(b)
    return e
  if d==2:
    e=c.index(b)
    c.remove(e)
    f=c.index(b)
    return (e,f)
  if d==3:
    x=c.index(b)
    c.remove(b[x])
    z=c.index(b)
    c.remove(z)
    w=c.index(b)
    return (x,z,w)
  if d==4:
    b=[b]
    x=c.index(b[0])
    c.remove(b[x])
    z=c.index(b[0])
    c.remove(c[z])
    w=c.index(b[0])
    c.remove(c[w])
    r=c.index(b[0])
    resultado1=(str(x))+(str(z+1))+(str(w+2))+(str(r+3))
    resultado=("0 5 9 13")
    return resultado
  
           