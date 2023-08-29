def buscarTodas(a,b):
    a=list(a)
    x=""
    i=0
    while i<len(a):
      if a[i]==b:
        x=x+str(i)+ " "
      i = i+1
    y=list(x)
    y.pop(len(x)-1)
    y="".join(y)
    return y

if __name__ == "__main__":
    pass
           