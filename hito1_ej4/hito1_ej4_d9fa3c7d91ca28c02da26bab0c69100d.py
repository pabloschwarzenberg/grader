#Conversión de Decimal a Binario
x=int(input(">"))
b=bin(x)
d=str(b).split("b")
f=int(d[1])
print("resultado=",f)