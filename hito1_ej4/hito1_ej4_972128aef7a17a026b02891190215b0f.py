#Conversión de Decimal a Binario
def convertirDecimalBinario(decimal):
 resultado = ""
 while decimal > 0:
  residuo = decimal % 2
  resultado = resultado + str(residuo)
  decimal = decimal // 2
 return resultado[::-1]
numero = int(input("ingrese el numero:"))
print("resultado = {0}".format(convertirDecimalBinario(numero)))
      