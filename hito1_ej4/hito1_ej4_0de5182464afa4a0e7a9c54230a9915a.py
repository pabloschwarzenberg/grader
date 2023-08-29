#Conversión de Decimal a Binario
decimal=int(input("Ingrese un número decimal: "))
binario=" "
while decimal>0:
    resto=decimal%2
    decimal=decimal//2
    binario=str(resto)+binario

print("resultado=",binario)
