#Conversión de Decimal a Binario
numero = int(input("Ingrese numero: "))
numerobinario= ""
while (numero>0):
    if (numero%2==0):
        numerobinario = str(0)+ numerobinario
    else:
        numerobinario = str(1)+numerobinario
    numero = numero//2
print("resultado="+str(numerobinario))