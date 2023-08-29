#Conversión de Decimal a Binario
#Entrada
num=int(input("Introduzca un número: "))
numBinario= 0

while num > 0:
    resto= num % 2
    num = num // 2
    numBinario= str(resto) + str(numBinario)
    
numBinario=(int(numBinario)//10)
print("Resultado=", numBinario)      