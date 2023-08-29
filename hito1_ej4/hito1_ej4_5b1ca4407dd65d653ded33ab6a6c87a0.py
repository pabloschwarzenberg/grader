#Conversión de Decimal a Binario
numero=float(input("Ingrese un numero decimal para convertir a binario:"))
resto=""
while numero//2!=0:
    resto=str(round(numero%2))+resto
    numero=numero//2
binario=str(round(numero))+resto
print("resultado=",binario)