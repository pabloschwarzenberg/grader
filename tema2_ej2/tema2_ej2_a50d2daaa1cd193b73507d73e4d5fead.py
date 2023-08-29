# completa el código de la función
def amigos(a,b):
  TSA=a
  resto=b
  if(a < 5 and b < 5):
    return False
  while(resto!=0):
    resto=TSA%resto
  if(resto==0):
    return True
  else:
    return False