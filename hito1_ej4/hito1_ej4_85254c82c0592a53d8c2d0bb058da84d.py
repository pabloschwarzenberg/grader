#Conversión de Decimal a Binario
n=int(input('Ingrese el número que desea convertir'))
b=[]
while n>0:
    d=n%2
    b.append(str(d))
    n=n//2
b.reverse()
print("resultado=" +''.join(b))      