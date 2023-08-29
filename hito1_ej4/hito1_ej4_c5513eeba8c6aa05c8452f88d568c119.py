#Conversión de Decimal a Binario
nd=int(input("ingrese un numero: "))
b=0
d=0
while (nd>0):
  n=nd%2
  nd=int(nd//2)
  b=b+n*(10**d)
  d=d+1
print("resultado=",b)

