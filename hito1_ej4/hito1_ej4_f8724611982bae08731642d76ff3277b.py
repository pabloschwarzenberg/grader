#Conversión de Decimal a Binario
n=int(input())
c=""
while n/2>=1:
  c+=str(n%2)
 
  n=n//2
 
print("resultado=","1"+c[::-1])