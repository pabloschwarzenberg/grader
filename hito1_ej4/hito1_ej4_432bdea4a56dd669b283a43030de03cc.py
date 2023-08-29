#Conversión de Decimal a Binario
x=int(input())
y=x
L=""
while y > 0:
  L+=str(y%2)
  y=y//2
L=L[::-1]
resultado="resultado="+L
print(resultado)