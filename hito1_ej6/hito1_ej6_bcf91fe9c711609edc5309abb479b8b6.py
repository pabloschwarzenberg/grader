#Ordenar tres números
x = int(input("Ingrese primer numero: "))
y = int(input("Ingrese segundo numero: "))
z = int(input("Ingrese tercer numero: "))
a = min(x,y,z)
b = max(x,y,z)
c = (x + y + z) - a - b
print(a,",",c,",",b)