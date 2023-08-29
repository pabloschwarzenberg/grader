#Ordenar tres números

a = int(input("ingrese el 1° numero: "))
b = int(input("ingrese el 2° numero: "))
c = int(input("ingrese el 3° numero: "))

x = min(a,b,c)
z = max(a,b,c)
y = (a+b+c)-x-z

print("los numeros ordenados son: ",x,",",y,",",z,) 