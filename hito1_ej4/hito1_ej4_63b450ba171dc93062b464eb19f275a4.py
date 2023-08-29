#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
  return ("{0:b}".format(decimal))


numero_decimal = int(input("Ingrese el número: "))
print("resultado=" + str(decimal_a_binario(numero_decimal)))
