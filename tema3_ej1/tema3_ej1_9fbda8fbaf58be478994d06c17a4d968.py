# completa el código de la función
def suma_divisores(a):
  ciclo=2
  nro_divisores=0
  suma_divisores=1
  primo= 1
  if a==1:
    primo=0
    return(suma_divisores-1,bool(primo))
  while ciclo < a :
      if a%ciclo == 0:
          suma_divisores= suma_divisores + ciclo    
      ciclo=ciclo + 1
  if suma_divisores > 1:
      primo=0
      return (suma_divisores,bool(primo))
  else:
      return (suma_divisores,bool(primo))
  
#suma_divisores(13)