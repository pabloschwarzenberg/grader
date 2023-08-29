# por favor escribe aquí tu función
import math
def es_primo(numero):
  factorial = (math.factorial(numero - 1) + 1) % numero

  if numero == 1:
    return False
  
  elif factorial == 0:
    return True

  else:
    return False
           