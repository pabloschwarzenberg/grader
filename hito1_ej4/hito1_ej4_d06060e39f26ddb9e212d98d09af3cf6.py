num= int(input("Ingrese un numero decimal: "))
numLen= len(str(num))
while not numLen==2:
    num=int(input("Numero invalido, ingrese un numero decimal: "))
    numLen= len(str(num))
numBinario=""
while num>0:
    if(num%2==0):
        numBinario= str(0)+ numBinario
    else:
        numBinario= str(1)+numBinario
    num = num//2
  

print("resultado=",numBinario)