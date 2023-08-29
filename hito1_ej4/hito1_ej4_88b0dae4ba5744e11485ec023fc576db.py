#Conversión de Decimal a Binario
numero = eval(input("Numero: "))
resultado = bin(numero)
final = resultado[2:]
print("resultado={}".format(final))