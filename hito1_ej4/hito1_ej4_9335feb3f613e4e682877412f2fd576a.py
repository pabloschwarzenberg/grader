numero = int(input("ingrese numero:"))
numBinario = ""
while (numero>0):
    print(numero)
    if (numero%2==0):
        numBinario = str(0)+numBinario
    else:
        numBinario = str(1)+numBinario
    numero = numero//2
print("resultado=", numBinario)
