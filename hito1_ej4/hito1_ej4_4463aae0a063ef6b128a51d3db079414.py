#Conversión de Decimal a Binario
import math
import array
n=int(input("Ingrese un número: "))
digits=math.trunc(math.log(n,2))
m=[]
if(n!=1):
    for i in range(digits+1):
        j=digits-i
        m.append(n//(2**j))
        n=n%(2**j)
elif(n==1):
    m.append(1)
B=0
for i in range(len(m)):
    j=digits-i
    B=B+m[i]*(10**j)
print("resultado=",B,sep="")