def suma_divisores():
  cuenta=0
  for n in range(1,a):
    if n==1:
      return(cuenta,False)
    else:
      if a%n==0:
        cuenta+=n
      else:
        pass
  if a==1:
    return(cuenta,False)
  elif cuenta>0 and cuenta>1:
    return(cuenta,False)
  else:
    return(cuenta,True)