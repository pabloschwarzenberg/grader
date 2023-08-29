# completa el código de la función
def suma_divisores(a):
    x = 0
    if a == 1:
      return (0,False)
    for i in range(1,a):
      if a%i == 0:
          x =x + i
    if x == 1:
      return (x,True)
    else:
      return (x,False)

  
           