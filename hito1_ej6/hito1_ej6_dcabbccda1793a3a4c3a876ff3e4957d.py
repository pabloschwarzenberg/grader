#Ordenar tres números
x=int(input("primer numero:"))
y=int(input("segundo numero:"))
z=int(input("tercer numero:")) 
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c 
print("el orden de los numeros es:",(a,b,c))
  
  
  
