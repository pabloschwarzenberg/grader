#Ordenar tres números
x = int(input("ingrese un numero:"))
y = int(input("ingrese un segundo numero:"))
z = int(input("ingrese un tercer numero:"))
mi = min(x,y,z)
m = max(x,y,z)
D = (x + y + z) - mi - m
print(mi ," , ", D , " , ", m)