#Conversión de Decimal a Binario
numero = int(input("Conversión de Decimal a Binario: "))

l = list(bin(numero))
l.pop(0)
l.remove("b")

numero = "".join(l)
print("resultado=",numero)