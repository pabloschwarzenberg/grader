#Conversión de Decimal a Binario
a=int(input("Ingrese un número:"))
b=""
while a/2>=(1/2):
   b+=str(a%2)
   a=(a//2)
print("resultado=",b[::-1])
