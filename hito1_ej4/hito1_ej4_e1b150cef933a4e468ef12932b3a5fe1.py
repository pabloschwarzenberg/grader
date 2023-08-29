#Conversión de Decimal a Binario
num = int(input())
convertidor = []
while num>=1:
    convertidor.insert(0,num%2)
    num = num // 2
binario = "".join(str(i) for i in convertidor)
print("resultado=",binario)