#Conversión de Decimal a Binario
num=float(input("INGRESAR NUMERO DECIMAL: "))
binario=""
while num!=0:
    resto=int(num%2)
    cuociente=int(num//2)
    binario=str(resto)+binario
    num=cuociente
print(binario)
