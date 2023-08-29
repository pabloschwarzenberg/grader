# por favor escribe aquí tu función
def es_primo(a):
  if a<2:
    return False 
  elif a==2:
    return True
  else:
    for n in range(2,a):
      if a%n==0:
        return False
      elif n==a-1:
        return True  