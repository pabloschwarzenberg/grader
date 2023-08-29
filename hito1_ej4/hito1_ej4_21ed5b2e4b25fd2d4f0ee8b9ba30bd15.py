#Conversión de Decimal a Binario
Decimal = int(input("Ingresar número decimal: "))

cadena = ""

while Decimal > 0:

 resto = str(Decimal%2)

 Decimal = int(Decimal/2)

 cadena = (resto+cadena)

print("resultado= ",(cadena))