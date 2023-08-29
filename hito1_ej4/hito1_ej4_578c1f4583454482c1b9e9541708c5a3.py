#Conversión de Decimal a Binario
n=int(input("Ingrese un numero: "))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append((a))
    n=(n-a)/2
k.reverse()
print("resultado=","".join(map(str, k)))