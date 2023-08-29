#Conversión de Decimal a Binario
decimal=int(input("ingrese el numero: "))
bin=" "
while decimal > 0:
    resto=decimal%2
    decimal=decimal//2
    bin=str(resto)+bin
print("resultado=",bin)      