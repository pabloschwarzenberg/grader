#Conversión de Decimal a Binario
x=float(input("introducir numero decimal: "))
bin=""
while x!=0:
  x_1=x%2
  x=x//2
  bin=str(int(x_1))+bin
print("Resultado=",bin)