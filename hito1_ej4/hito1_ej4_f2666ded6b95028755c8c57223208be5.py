#Conversión de Decimal a Binario
x=int(input("Numero:"))
b=""
while x>=1:
   y=x%2
   x=x//2
   b=str(y)+b
   print("resultado=",b)
       
     