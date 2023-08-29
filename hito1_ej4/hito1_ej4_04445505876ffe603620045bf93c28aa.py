#Conversión de Decimal a Binario
a = int(input("conversion de decimal a binario: "))

i=list(bin(a))
i.pop(0)
i.remove("b")

a="".join(i)
print("resultado= ",a)