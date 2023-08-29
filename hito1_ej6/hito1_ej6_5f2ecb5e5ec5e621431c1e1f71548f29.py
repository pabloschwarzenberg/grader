#Ordenar tres números
a = int(input("primer numero:"))
b = int(input("segundo numero:"))
c = int(input("tercer numero:"))
 
x=min(a,b,c)
y=max(a,b,c)
z=(a+b+c)-x-y
print("el orden de los numeros es:",(x,z,y))