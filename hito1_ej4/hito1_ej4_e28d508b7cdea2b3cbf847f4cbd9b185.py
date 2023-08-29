#Conversión de Decimal a Binario
N=int(input())
x=""

while N>0 :
  a=(N-2*(N//2))
  N=(N//2)
  x=str(a)+x
  
print("resultado=",x)