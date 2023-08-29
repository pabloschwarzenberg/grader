def numero_perfecto(t):
  con_tador=1
  su_ma=0
  while con_tador!=t:
    if t%con_tador==0:
      su_ma=su_ma+con_tador
    con_tador=con_tador+1
  if su_ma==t:
    return True
  else:
    return False

if __name__=="main":
  t=eval(input("Ingrese su numero: "))
  if numero_perfecto(t):
    print("El numero {0} es perfecto".format(t))
  else:
    print("El numero {0} no es perfecto".format(t))
