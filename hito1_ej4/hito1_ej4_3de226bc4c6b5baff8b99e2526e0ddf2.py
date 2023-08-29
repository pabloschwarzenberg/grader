#Conversión de Decimal a Binario
#para dar vuelta la str a, a = a[::-1]
n=int(input())
r = ""
while n>=2:
    r=str(n%2)+r
    n=n//2
   
print("resultado= ",str(n)+r)