#Conversión de Decimal a Binario
numero=int(input("numero: "))
while (numero!=0):
    if numero%2!=0:
        print(1)
    elif numero%2==0:
        print(0)
    numero=int(numero/2)