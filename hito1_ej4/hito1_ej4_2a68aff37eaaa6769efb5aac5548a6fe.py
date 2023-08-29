#Conversión de Decimal a Binario
a = int (input("Conversion de numero decimal a binario: "))

x= list(bin(a))
x.pop(0)
x.remove("b")

a = "".join(x)
print("El resultado es: ",a)
