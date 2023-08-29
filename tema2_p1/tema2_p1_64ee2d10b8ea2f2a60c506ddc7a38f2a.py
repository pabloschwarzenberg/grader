# por favor escribe aquí tu función
def es_primo(num, n=2):
      if num == 1: 
        return False
      if num > 1:
        cont = 0
        for i in range(n,num):
          resta = num%i
          if resta == 0:
            cont += 1
        if cont == 0:
          return True
        else:
          return False