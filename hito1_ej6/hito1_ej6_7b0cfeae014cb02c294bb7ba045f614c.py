#Ordenar tres números
x = int(input(" inserte un numero: "))
y = int(input(" inserte otro numero: "))
z = int(input("inserte un ultimo numero: "))

a = min(x, y, z)
b = max(x, y, z)
c = (x + y + z)- a - b

print(a,",",c,",",b)
