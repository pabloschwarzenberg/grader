#Conversión de Decimal a Binario
numero = int(input("ingrese numero"))
numbinario=""
while (numero>0):
    if (numero%2==0):
        numbinario=str(0)+ numbinario
    else:
        numbinario=str(1)+numbinario
    numero = numero//2
    print("resultado=",numbinario)     