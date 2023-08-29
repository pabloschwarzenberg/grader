#Conversión de Decimal a Binario
num=float(input("Ingrese un número:"))
binario=""
while num!=0:
    if num%2==0:
        binario="0"+binario
    if num%2==1 or num==1:
        binario="1"+binario
    num=num//2
print("resultado=",binario)