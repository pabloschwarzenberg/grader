# por favor escribe aquí tu función  
def es_primo(numero):
  if numero == 1:
      return False
  for i in range(2, numero):
    if numero % i == 0:
      print("no es primo")
      return False
    
  print("es un numero primo")
  return True

           