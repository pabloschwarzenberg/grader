# completa el código de la función
def suma_divisores(a):
  div=2
  cant=0
  while div <= a:
    if a%div==0:
      cant=cant+1
      div=div+1
    else:
      div=div+1
      
  if cant==2:
    return (div,True)
  else:
    return (div,False)