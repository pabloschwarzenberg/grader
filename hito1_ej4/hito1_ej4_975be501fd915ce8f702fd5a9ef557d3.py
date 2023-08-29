#Conversión de Decimal a Binario
num=int(input("Ingrese número:")) 

Numero=num 
lista=[num] 
binario=[]
m=""
for i in range(1,num): 
    num=num//2 
    if num==0: 
        num=0 
        break 
    lista.append(num) 
for x in lista: 
    if (x)%2>0: 
        numbinario=1 
    if (x)%2==0 or x==0: 
        numbinario=0 
    binario.append(numbinario)
for y in reversed(binario):
    m=m+str(y)
print("resultado="+m)