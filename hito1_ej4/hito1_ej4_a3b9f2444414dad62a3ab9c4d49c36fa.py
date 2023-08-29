#Conversión de Decimal a Binario
from math import floor
numero=int(input('Ingrese numero para convertir a binario: '))
lista=[]
for i in range(numero):
    if numero!=0 and numero%2==0:
        lista.append(0)
        numero=floor(numero/2)
        
    elif numero!=0 and numero%2==1:
        lista.append(1)
        numero=floor(numero/2)
    
print('resultado=',end="")
for i in reversed(lista):
    print(i,end="")
          