# por favor escribe aquí tu función
def es_primo(num):
  div=1
  cant=0
  while div <= num:
    if num%div==0:
      cant=cant+1
      div=div+1
    else:
      div=div+1
      
  if cant==2:
    return True
  else:
    return False
    
 