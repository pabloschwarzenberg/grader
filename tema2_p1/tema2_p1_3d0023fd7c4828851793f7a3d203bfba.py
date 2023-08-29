# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(Numero):
  if Numero > 1:
    a = 0
    divisor = 2
    while divisor < Numero:
      resto = Numero % divisor
      if resto == 0:
        a += 1
      divisor += 1
    if a == 0:
      return True
    else:
      return False
  else:
    return False
try:
  Numero_ingresado = int(input("ingrese un número: "))
  print(es_primo(Numero_ingresado))
except:
  print("ingrese un solo numero")           