#Conversión de Decimal a Binario
numero_decimal =int(input("ingrese un numero para convertir a binario: "))

temp = "{0:b}".format(numero_decimal)

print(temp)