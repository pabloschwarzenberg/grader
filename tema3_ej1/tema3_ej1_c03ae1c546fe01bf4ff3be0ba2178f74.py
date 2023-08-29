# completa el código de la función
def suma_divisores(a):
  A=0
  if a<=2:
    return (0,False)
  else:
    for i in range(1,a):
      if a%i==0:
        A+=i
    if A==1:
        return A,True
    else:
        return A,False
print(suma_divisores(13))