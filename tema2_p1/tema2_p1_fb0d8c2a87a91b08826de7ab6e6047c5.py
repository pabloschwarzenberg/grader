# por favor escribe aquí tu función
def es_primo(numero):
  if(numero==1):
    return False
  elif(numero%2!=0 and numero%3!=0 and numero%5!=0 and numero%7!=0):
    return True
  elif(numero==2 or numero==3 or numero==5 or numero==7):
    return True
  else:
    return False
           