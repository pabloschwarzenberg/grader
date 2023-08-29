#Conversión de Decimal a Binario
a = int(input("Conversión de Decimal a Binario: "))

l = list(bin(a))
l.pop(0)
l.remove("b")

a = "".join(l)
print("resultado=",a)   