#Conversión de Decimal a Binario
num = int(input("ingrese un numero: "))
numb = bin(num)[2:]
numb = int(numb)
print("resultado=",numb)