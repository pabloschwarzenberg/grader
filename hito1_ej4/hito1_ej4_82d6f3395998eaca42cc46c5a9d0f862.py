#Conversión de Decimal a Binario
num = int(input("Ingrese un numero: "))
list = []

while num >= 1:
    list.insert(0, num%2)
    num = num //2
resultado = "".join(str(i) for i in list)
print("resultado=", resultado)      