#Conversión de Decimal a Binario
numero=int(input("ingrese un numero: "))
numerobinario=""
while(numero>0):
    if(numero%2==0):
        numerobinario=str(0)+numerobinario
        
    elif(numero%2!=0):
        numerobinario=str(1)+numerobinario
    numero=numero//2
print("resultado=",numerobinario)