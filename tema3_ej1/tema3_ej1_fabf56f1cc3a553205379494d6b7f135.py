# completa el código de la función
def suma_divisores(a):
  i=1  
  b=list()
  while i<a:
        if a%i==0:
          b.append(i)
        i=i+1
  g=sum(b)
  if g==1:
    return (g,True)
  else:
    return (g,False)
   
if __name__ == "__main__":
    pass
           