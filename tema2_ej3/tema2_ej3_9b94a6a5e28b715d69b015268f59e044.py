def numero_perfecto(numero):
  divisor = 0
  cociente = 0
  suma = 0
  retorno = False
  for i in range(numero):
    divisor = i+1
#asi valida divisores de dividendo
    if numero%divisor == 0 and divisor != numero:
      suma = divisor + suma
      print(divisor)

  if suma == numero:
    retorno = True

  return retorno
if __name__=="__main__":
  numero = int(input("numero: "))
  print(numero_perfecto(numero))
           