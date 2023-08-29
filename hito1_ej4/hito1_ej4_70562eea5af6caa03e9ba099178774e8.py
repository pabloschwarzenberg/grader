#Conversión de Decimal a Binario
x = int(input())
n = []

while x>=1:
    n.insert(0,x%2)
    x//=2
r = "".join(str(i) for i in n)
print("resultado=",r)  