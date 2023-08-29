#ordenar tres numeros
#ordenar tres numeros de menor a mayor#

a=int(input("escriba el primer numero: "))
b=int(input("escriba el segundo numero: "))
c=int(input("escriba el tercer numero: "))

x=min(a,b,c)
y=max(a,b,c)
z=(a+b+c)-x-y

print("los numero son",(x,z,y))      