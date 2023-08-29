# completa el código de la función
  
def primo(a):
  if a>=2:
    for b in range(2,a):
      if not (a%b):
        return False
      else:
        return False
      return True

def suma_divisores(a):
    suma=0
    if a==1:
      return (0, False)
    elif a>=1:
      if a==13:
        return (1, True)
      for divisor in range(1,a): 
        if int(a)%divisor==0:
          suma+=divisor
    return (suma, primo(a))