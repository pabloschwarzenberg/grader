# por favor escribe aquí tu función
def es_primo(numero):
  if numero > int(1):
      ZERO = 0
      DOS = 2
      while DOS < numero:
          Z= numero % DOS
          if Z == 0:
              ZERO= ZERO + 1
          DOS= DOS + 1
      if ZERO == 0:
       return True
      else:
        return False

  else:
        return False