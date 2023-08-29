#Conversión de Decimal a Binario
print("Conversor")

a=int(input("Número Decimal:"))
b=""


while a>0:
      c=int(a%2)

      b=str(c)+b
      e=a-c
      a=e/2

      
print("Resultado=",b)
