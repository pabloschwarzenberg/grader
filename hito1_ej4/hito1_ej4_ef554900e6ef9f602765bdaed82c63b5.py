#Conversión de Decimal a Binario
# Ingreso de numero
numero=int(input("Ingrese numero: "))
# Conversion a binario
numero_binario=str(bin(numero))
numero_binario=int(numero_binario[2:])
print("Resultado=",numero_binario)