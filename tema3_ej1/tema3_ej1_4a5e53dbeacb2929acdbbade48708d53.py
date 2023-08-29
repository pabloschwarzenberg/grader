# completa el código de la función
def divisores(f):
    divisores=[]
    w=f
    for f in range(1,f):
        if(w/f==w//f):
            divisores.append(f)
    return(divisores)
def suma_divisores(a):
  y=0
  for g in divisores(a):
      y=y+g      
  if(y==1):
      return(y,True)
  if(y!=1):
      if(y>1):
       return(y,False)
  if(divisores(a)==[]):
      return(0,False)
           