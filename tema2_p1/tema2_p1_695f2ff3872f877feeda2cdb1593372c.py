def es_primo(numero):
  a = 0
  for i in range(1,numero+1):
    if(numero%i) == 0:
      a = a+1
  if(a!=2):
    return False
  else:
    return True
    

