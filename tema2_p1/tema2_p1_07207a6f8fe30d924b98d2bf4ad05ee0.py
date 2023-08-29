# por favor escribe aquí tu función
def es_primo(digito):
    if digito<2:
       return False  
    for num in range(2,digito):
       if digito % num ==0:
          return False
       return True    