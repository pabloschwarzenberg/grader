#Conversión de Decimal a Binario
a = int(input("Conversión de D a B: "))

l = list(bin(a))
l.pop(0)
l.remove("b")

a = "".join(l)
#print
print("resultado=",a)