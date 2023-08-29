#Conversión de Decimal a Binario
      def decimal_a_binario(decimal):
  return binario(decimal)[2:]

n=int(input("Ingrese número "))
bin= decimal_a_binario(n)
print(binario)