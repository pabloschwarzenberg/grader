# completa el código de la función
def suma_divisores():
  if __name__ == "__main__":
    a=int(input())
  cuenta=0
  for n in range(1,a):
    if n==1:
      return(cuenta,False)
    else:
      if a%n==0:
        cuenta=cuenta+n
      else:
        pass
  if a==1:
    return(cuetna,False)
  elif cuenta>0 and cuenta>1:
    return(cuenta,False)
  else:
    return(cuenta,True)
def suma_divisores(a):
  cuenta=0
  for n in range(1,a):
    if a==1:
      return(cuenta,False)
    else:
      if a%n==0:
        cuenta=cuenta+n
      else:
        pass
  if a==1:
    return (cuenta,False)
  elif cuenta>0 and cuenta>1:
    return(cuenta,False)
  else:
    return(cuenta,True)




