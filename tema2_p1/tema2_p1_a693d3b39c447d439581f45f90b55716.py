# por favor escribe aquí tu función
def es_primo(numero):
  contador = 2
  flag = True
  while contador<numero:
   if (numero%contador) == 0:
     flag = False
   contador = contador + 1
  if numero == 1:
    flag = False
  return flag
           