x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
z = int(input("Ingrese el tercer numero: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print(a,",",b,",",c)