#Conversión de Decimal a Binario
decimal = int(input("ingrese numero decimal: "))
numero_binario = " "

while decimal > 0: 
     decimal1 = decimal%2
     decimal=decimal//2
     numero_binario= str(decimal1) + numero_binario
     
print("resultado= ", numero_binario)
     
