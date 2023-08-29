#Conversión de Decimal a Binario
numero = eval(input("Ingrese numero: "))
Bin = ""

while numero > 0:
    if numero%2 == 0:
        Bin = "0" + Bin
    elif numero%2 != 0:
        Bin = "1" + Bin

print("El resultado es: ", Bin)