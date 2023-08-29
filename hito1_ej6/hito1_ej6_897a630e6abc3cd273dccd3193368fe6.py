#Ordenar tres números
x=int(input("escriba el numero 1:"))
y=int(input("escriba el numero 2:"))
z=int(input("escriba el numero 3:"))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c

print("los numeros ordenados de menor a mayor son:{},{},{}".format(a,b,c))