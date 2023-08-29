# por favor escribe aquí tu función
def divisores(n):
    divisor=1
    cantidad_divisores=0
    while divisor <= n:
        if n%divisor==0:
            cantidad_divisores=cantidad_divisores+1
        divisor=divisor+1
    return cantidad_divisores
def es_primo(numero):
    if divisores(numero)==2:
      return True
    else:
      return False

           