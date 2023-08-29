# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(numero):
    # Verificar si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Verificar si el número es divisible por algún número menor que él
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    # Si no es divisible por ningún número menor que él, es primo
    return True           