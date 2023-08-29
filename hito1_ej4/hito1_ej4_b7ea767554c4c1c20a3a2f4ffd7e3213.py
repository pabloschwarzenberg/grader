#Conversión de Decimal a Binario
x=int(input("igrese el numero"))
z=1
l=[]
while z!=0:
 y=x%2
 l.append(y)
 z=x//2
 x=z
lr=l[::-1]
r="".join(map(str, lr))
print("resultado=", r)      