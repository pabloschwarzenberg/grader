# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(numero):
    contador = 1
    divisor = 1
    while (divisor < numero):
        if numero % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1
    if contador == 2:
        valor = True
    elif contador != 2:
        valor = False
    return valor           