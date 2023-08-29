#Conversión de Decimal a Binario
numero = int(input("Ingrese un número: "))
new = bin(numero)
new1 = str(new)
new2 = new[2:]
final = int(new2)
print("resultado=",final)