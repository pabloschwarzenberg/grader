# por favor escribe aquí tu función
def es_primo(numero):
  Divisor = 2
  I = 0
  while I < numero:
    Numero = numero / Divisor
    Numero2 = numero // Divisor
    I += 1
    Divisor += 1
    if numero == 1:
      numero = False
      break
    elif Numero == 1.0:
      numero = True
      break
    elif Numero == float(Numero2):
      numero = False
      break
  return numero