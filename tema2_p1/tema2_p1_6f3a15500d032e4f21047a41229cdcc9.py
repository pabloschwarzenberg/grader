# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

# Ejemplos de uso
print(es_primo(7))  # True
print(es_primo(10))  # False
print(es_primo(23))  # True
           