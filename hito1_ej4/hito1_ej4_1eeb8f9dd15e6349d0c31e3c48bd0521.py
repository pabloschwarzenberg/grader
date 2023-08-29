#Conversión de Decimal a Binario
     
x = int(input("Ingrese el número que desea convertir: "))

l = list(bin(x))

l.pop(0)

l.remove("b")


x = "".join(l)

print("resultado=",x)
