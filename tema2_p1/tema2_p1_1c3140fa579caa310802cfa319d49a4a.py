# por favor escribe aquí tu función
def es_primo(numero):
  for i in range(2,numero):
    if (numero%i) == 0:
      return False
  return True
  
 def entrada():
  numero=int(input('Ingrese un numero:'))
  es_primo(numero)
  resultado=es_primo(numero)
  print(resultado)
entrada()

           