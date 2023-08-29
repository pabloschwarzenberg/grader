def buscarTodas(a,b):
  a=list(a)
  #print(a)
  c=[]
  try:
    for i in a:
      z=a.index(b)
      #print(z)
      c.append(z)
      if a[z]!="_":
        a[z]="_"
  except ValueError:
    c=" ".join(map(str, c))
    
    return c


if __name__ == "__main__":
    pass
           