def numero_perfecto(a):
  ciclo=2
  nro_divisores=0
  suma_divisores=1
  numero_perfecto= 0
  if a==1:
    numero_perfecto=0
    return(bool(numero_perfecto))
  while ciclo < a :
      if a%ciclo == 0:
          suma_divisores= suma_divisores + ciclo    
      ciclo=ciclo + 1
  if suma_divisores ==a:
      numero_perfecto=1
      return(bool(numero_perfecto))
  else:
      return(bool(numero_perfecto))