# por favor escribe aquí tu función
def es_primo(numero):
    divisores = 0
    for i in range(1,numero+1):
        if numero%i == 0:
            divisores = divisores + 1
    next

    if divisores == 2:
      return True            
    else:
      return False
     

