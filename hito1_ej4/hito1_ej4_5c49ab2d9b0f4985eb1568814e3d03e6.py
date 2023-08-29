#Conversión de Decimal a Binario
x=int(input("ingrese numero"))
z=""
while x>=2:
    z=str(x%2)+z
    x=(x//2)
print("resultado=",z)