#Ordenar tres números
x = float (input("Indique el primer numero: "))
y = float (input("Indique el segundo numero: "))
z = float (input("Indique el tercero numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("los numero de menor a mayor son: ".format(a,b,c))
