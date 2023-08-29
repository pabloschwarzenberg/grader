# por favor escribe aquí tu función

  
def es_primo(n):
  divisor=2
  while divisor<n:
    if n%divisor==0:
      return(False)
      break
    else:
      divisor+=1
  if n==divisor:
    return(True)
  elif n==1:
    return(False)

