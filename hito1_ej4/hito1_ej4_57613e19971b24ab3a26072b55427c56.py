#Conversión de Decimal a Binario
#Entrada
num = float (input ("Ingrese el número a convertir:   "))
#Procedimiento
b = bin(int(num))
c = b[2::]
print("resultado:" + c)