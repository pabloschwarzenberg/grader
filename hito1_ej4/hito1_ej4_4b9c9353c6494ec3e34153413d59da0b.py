#Conversión de Decimal a Binario
x= int(input('Numero decimal: '))
bin=""
while x//2 !=0:
    bin = str(x%2)+bin
    x=x//2
bin=str(x)+bin
print("resultado="+bin)
