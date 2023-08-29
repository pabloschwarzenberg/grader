# por favor escribe aquí tu función
def es_primo(numero):
  n=0
  x=1
  while True:
    r=numero/x
    R=numero//x
    if(x==numero):
      break
    if(r==R):
      n=n+1
    x=x+1
  if(n==1):
    return(True)
  else:
    return(False)
           