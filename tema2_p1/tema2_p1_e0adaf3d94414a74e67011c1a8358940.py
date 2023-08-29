# por favor escribe aquí tu función   
def es_primo(num):
  if num > 1:
    for i in range(2, num):
      if(num % i) == 0:
        return False 
    else: 
        return True
  else:
       return False

      