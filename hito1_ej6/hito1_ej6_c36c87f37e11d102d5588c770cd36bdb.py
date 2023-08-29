#Ordenar tres números
n1=int(input("n1"))
n2=int(input("n2"))
n3=int(input("n3"))
x=min(n1,n2,n3)
y=max(n1,n2,n3)
 
z=(n1+n2+n3)-x-y
print("El orden es:",(x,z,y)) 
 