numero = int(input("Ingrese numero"))
numBinario = ""
while(numero>0):
    if(numero%2==0):
        numBinario = str(0)+ numBinario
    else:
        numBinario = str(1)+ numBinario
    numero = numero//2
print("resultado=", numBinario)