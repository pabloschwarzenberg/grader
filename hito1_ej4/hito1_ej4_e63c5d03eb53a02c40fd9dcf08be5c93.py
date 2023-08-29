#Conversión de Decimal a Binario
binario = " "
while decimal // 2 != 0:
      binario = str(decimal % 2) + binario
      decimal = decimal // 2
return str(decimal) + binario

numero = int(input('Introduce el número que deseas convertir a binario:'))
print(convbinario(numero))    