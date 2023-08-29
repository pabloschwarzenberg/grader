def suma_divisores(x):
  cycle=2
  numdiv=0
  sumadiv=1
  numero= 1
  if x==1:
    numero=0
    return(sumadiv-1,bool(numero))
  while cycle < x :
      if x%cycle == 0:
          sumadiv= sumadiv + cycle   
      cycle=cycle + 1
  if sumadiv > 1:
      numero=0
      return (sumadiv,bool(numero))
  else:
      return (sumadiv,bool(numero))
