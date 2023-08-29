#Ordenar tres números
x = int(input("escribe el numero:"))
y = int(input("escribe el numero:"))
z = int(input("escribe el numero:"))

a= min(x,y,z)
c= max(x,y,z)
b= (x + y + z)-a-c
print("Los numero ordenados son:{},{},{}".format(a,b,c))