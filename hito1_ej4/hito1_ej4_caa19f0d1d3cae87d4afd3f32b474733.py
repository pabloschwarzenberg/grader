#Conversión de Decimal a Binario
def Decimal_a_Binario(numero):
  Resultado = ""
  if numero == 0:
    return "0"
  while numero > 0:
    residuo = numero  % 2
    Resultado = str(residuo) + Resultado
    numero  = numero // 2
  return Resultado  
  
numero_decimal = int(input("Ingrese un numero decimal:"))
numero_binario = Decimal_a_Binario(numero_decimal)
print("Resultado=" + numero_binario)