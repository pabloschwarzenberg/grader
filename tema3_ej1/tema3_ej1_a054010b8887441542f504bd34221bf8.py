# suma de divisores x fase pri
def suma_divisores(x):
  fase=2
  divisoresnum=0
  agregar=1
  #numeros primos
  pri= 1
  #si x==1 return
  if x==1:
    pri=0
    return(agregar-1,bool(pri))
  while fase < x :
  #division de fase ==o suama 
      if x%fase == 0:
          agregar= agregar + fase    
      fase=fase + 1
  if agregar > 1:
      pri=0
      return (agregar,bool(pri))
      #si no retur agregar pri
  else:
      return (agregar,bool(pri))
           