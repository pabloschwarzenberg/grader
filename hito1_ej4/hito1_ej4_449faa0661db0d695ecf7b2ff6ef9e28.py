#Conversión de Decimal a Binario
x=float(input("Ingrese un número decimal: "))
bin= ""
while x // 2 != 0:
    resto=int(x%2)
    x=int(x/2)
    bin=str(resto)+bin
bin=str(1)+bin        
print("resultado=",bin)      