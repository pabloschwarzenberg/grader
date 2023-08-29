#Conversión de Decimal a Binario
import math

numero=int(input('ingrese un numero decimal:')
binario= "z"
if (numero>0):
  while(numero>0):
      if (numero%2==0):
          binario = "0" + binario
      else:
          binario= "1" + binario
      numero =int(math.floor(numero/2))
else:
    if (numero==0):
      binario= "o"
    else:
        binario = 'no se pudo pasar a binario pruebe con un numero positivo'