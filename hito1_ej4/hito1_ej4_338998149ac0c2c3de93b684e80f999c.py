#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número: "))
binario = 0
auxiliar2 = 0
auxiliar = decimal
while (auxiliar > 0):
    binario=((auxiliar%2)*(10**auxiliar2))+binario
    auxiliar = int(auxiliar / 2)
    auxiliar2 += 1
x = decimal
y = binario
print("El binario de", x, "es", y)