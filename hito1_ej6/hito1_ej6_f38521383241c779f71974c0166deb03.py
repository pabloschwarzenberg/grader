#Ordenar tres números
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))
c = int(input("Ingrese un numero entero: "))
x = min(a, b, c)
z = max(a, b, c)
y = (a+b+c)-x-z
print(str(x) + ","+str(y)+","+str(z))
