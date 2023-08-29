# por favor escribe aquí tu función
def es_primo(numero):
    Esprimo = True
    if numero == 1:
       Esprimo = False
    else:
        for x in range(2, numero-1):
           if numero % x == 0:
              Esprimo = False
              break
    return Esprimo
