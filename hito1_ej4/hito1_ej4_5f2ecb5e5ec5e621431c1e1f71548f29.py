#Conversión de Decimal a Binario
num=int(input("Ingrese numero decimal: "))
conver=""
while ((num // 2)!= 0):
    conver=str(num%2)+conver
    num=num//2
conver=str(num)+conver
print("resultado="+conver)      