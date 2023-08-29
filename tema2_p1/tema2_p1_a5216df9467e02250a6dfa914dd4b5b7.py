# por favor escribe aquí tu función
def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    if numero==1:
      return False
    else:
      print("Es primo")
      return True
           