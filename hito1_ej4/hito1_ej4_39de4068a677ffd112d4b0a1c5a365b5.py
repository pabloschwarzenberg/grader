#Conversión de Decimal a Binario
num = int(input("Introduce el número a cambiar de base: "))
trans = " "
while num // 2 != 0:
        trans = str(num % 2) + trans
        num = num // 2
        resultado= str(num) + trans
print("resultado=",resultado)
