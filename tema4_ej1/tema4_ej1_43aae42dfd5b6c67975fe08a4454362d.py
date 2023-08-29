import random
def ocultar_letras(palabra,cantidad):

  x=len(palabra)-1
  
  def numero_al(y,z):
    z=[]
    y=random.randint(1,x)
    for n in z:
      if y==n:
        while y==n:
          y=random.randint(1,x)
          z.append(y)
          return z, y, True
      if y!=n:
        z.append(y)
        return z, y, True
      
  palabra_l=list(palabra)
  n=0
  while n<cantidad:
    n=0
    if numero_al==True:
      palabra_l[y]='_'
    n=n+1
    return palabra 
  return palabra    
def revisar_letra(palabra_secreta,palabra,letra):
    return palabra
  
if __name__ == "__main__":
    pass
         