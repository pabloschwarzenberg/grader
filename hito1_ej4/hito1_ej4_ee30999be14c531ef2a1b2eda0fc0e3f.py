#Conversión de Decimal a Binario
def decimalABinario(numeroDecimal):
  numeroBinario = 0
  multiplicador = 1
  while numeroDecimal != 0:
     numeroBinario = numeroBinario + numeroDecimal % 2 * multiplicador
     numeroDecimal //= 2
     multiplicador *= 10
  return numeroBinario
numero=int(input())
print("resultado=",end="")
print(decimalABinario(numero))