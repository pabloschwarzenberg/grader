#Conversión de Decimal a Binario
a=int(input("Ingrese un numero: "))
b=2
s=''
while not a==0:
    r=str(a%b)
    s=r+s
    a=a//b
    
print('Resultado=',s)
          