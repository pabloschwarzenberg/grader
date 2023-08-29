#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y

print("El orden de los numeros de menor a mayor es:", x,",",z,",",y)     