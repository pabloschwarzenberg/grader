#Conversión de Decimal a Binario
def DecimalABinario(decimal):
  resultado = " "
  
  while decimal > 0:
    residuo = decimal % 2
    resultado = resultado + str(residuo)
    decimal = decimal // 2
    
  return resultado[::-1]
    
decimal = int(input("Ingresa el numero que quieras convertir a binario: ")) 

print("resultado= ", DecimalABinario(decimal))