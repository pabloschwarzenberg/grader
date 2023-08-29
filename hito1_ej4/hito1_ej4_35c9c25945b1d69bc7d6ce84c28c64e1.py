#Conversión de Decimal a Binario

X = int(input("Conversión de Decimal a binario= "))

l = list(bin(X))
l.pop(0)
l.remove("b")

X = "".join(l)

print("resultado=",X)