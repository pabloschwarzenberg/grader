#Conversión de Decimal a Binario
numero=int(input("ingrese un numero: "))
binario = "";
while(numero!=1):
 binario = str((numero%2)) +  binario
 numero = numero // 2
binario = str(numero) + binario
print("resultado=",binario )      