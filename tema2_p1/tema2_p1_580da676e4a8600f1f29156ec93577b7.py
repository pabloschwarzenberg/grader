# por favor escribe aquí tu función

numero=eval(input('numero: '))
def es_primo(numero):
  if numero==2:
    return False
  if numero > 1:
    es = True
    for i in range(2, numero // 2 + 1):
        if not(numero % i):
            es = False
            break

    return es
  else:
    return False
resultado=es_primo(numero)
print(resultado)