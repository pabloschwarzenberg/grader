#Conversión de Decimal a Binario
numero=eval(input("ingresa un n°: "))
entero=int(numero)
binario=bin(entero)
comienzaEn=str(binario)[2:10000000000000000000]
print ("resultado=",comienzaEn)