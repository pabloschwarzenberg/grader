# por favor escribe aquí tu funció
def es_primo(num):
  if num ==2:
      return True
  else:
    for i in range(2,num):
        if not (num %i == 0):
            return True
        else:
            return False
    return False    