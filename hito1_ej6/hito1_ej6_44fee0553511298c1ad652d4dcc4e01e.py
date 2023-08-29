#Ordenar tres números
x=int(input("n1:"))
y=int(input("n2:"))
z=int(input("n3:"))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("el orden de los numeros de menor a mayor es:",(a,b,c))
