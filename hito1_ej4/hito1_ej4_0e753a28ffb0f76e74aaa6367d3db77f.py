#Conversión de Decimal a Binario
numero=(int(input("Ingrese el número que desea convertir\n")))
binario=""
while numero//2 !=0:
    binario= str (numero%2) + binario
    numero = numero//2
binario=str(numero)+binario
print("Resultado="+binario)