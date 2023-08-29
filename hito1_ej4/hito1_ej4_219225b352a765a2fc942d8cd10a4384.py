#Conversión de Decimal a Binario
#ENTRADA
decimal = input("ingrese un numero decimal: ")

#PROCESO
numero = int(decimal)
i=0
binario = ""
while(numero != 0):
    if(numero % 2) != 0 :
        binario += "1"
    else:
        binario += "0"
        
    numero = numero // 2

#SALIDA
print("resultado=",binario[::-1])