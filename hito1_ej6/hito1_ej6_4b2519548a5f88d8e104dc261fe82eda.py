#Ordenar tres números
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
z = int(input("Ingrese un numero: "))

a = min(x, y, z)
c = max(z, y, x)
b = (x + y + z) - ( a + c )

print(a,",", b,",", c)   