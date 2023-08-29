def buscarTodas(a,b):
    c=[]
    i=-1
    j=0
    h=0
    l=[]
    while j<len(a):
      d=a.find(b,h)
      if d==-1:
        break
      else:
        c.append(d)
        c.append(" ")
      h=d+1
      j=j+1
    c.pop(len(c)-1)
    k=0
    while k<len(c):
       l.append(str(c[k]))
       k=k+1
    l="".join(l)
    return l

if __name__ == "__main__":
    pass
           