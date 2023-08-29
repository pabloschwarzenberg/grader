#Conversión de Decimal a Binario
num=int(input('ingrese un numero:'))
bi=''
while num//2!=0:
  bi=str(num%2)+bi
  num=num//2
r='resultado='+str(num)+bi
print(r)