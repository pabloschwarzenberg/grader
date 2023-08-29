#Conversión de Decimal a Binario
x = int(input("Conversión de Decimal a Binario: "))

l = list(bin(x))
l.pop(0)
l.remove("b")

x = "".join(l)
print("resultado=",x)    