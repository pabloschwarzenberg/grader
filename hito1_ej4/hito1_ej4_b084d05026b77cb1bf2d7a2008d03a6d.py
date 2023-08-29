#Conversión de Decimal a Binario
n= int(input())
b=[]
f=""
while n >= 1:
    n_1=n%2
    b.append(n_1)
    n=n//2
b.reverse()
for i in range(0, len(b)):
    f= f + str(b[i])
print("resultado=",f)