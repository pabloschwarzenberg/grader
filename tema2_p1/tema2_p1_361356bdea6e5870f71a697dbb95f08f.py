def es_primo(numero):
  if(numero == 1):
    return False
  elif(numero%2 != 0):
    return True
  else:
    if(numero%2 == 0):
      return False