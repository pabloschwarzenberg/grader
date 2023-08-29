#Conversión de Decimal a Binario
num = int(input("Ingrese un número :"))

listabinarios = []

while num > 0 :
    digito = num % 2
    listabinarios.append(str(digito))
    num = num //2
listabinarios.reverse()

print("resultado="+''.join(listabinarios))