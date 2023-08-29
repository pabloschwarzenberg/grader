#Conversión de Decimal a Binario
num=int(input("Ingrese un numero"))
num=bin(num)
num=str(num)
num=num.replace("0b","")
num=int(num)
print("resultado=",num)