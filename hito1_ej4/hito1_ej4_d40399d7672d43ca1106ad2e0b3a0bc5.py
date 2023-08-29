#Conversión de Decimal a Binario
#Entradas
numero = int(input("Ingrese un número: "))

#Procesos

resultado = str(bin(numero))
print("Resultado=",resultado.lstrip("0b"))
