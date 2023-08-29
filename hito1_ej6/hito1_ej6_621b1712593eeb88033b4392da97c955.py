#Ordenar tres números 
a=int(input("primer numero:"))
b=int(input("segundo numero:"))
c=int(input("tercer numero:"))

x=min(a,b,c)
z=max(a,b,c)
y=(a+b+c)-x-z
print("orden:",(x,y,z))
  
  