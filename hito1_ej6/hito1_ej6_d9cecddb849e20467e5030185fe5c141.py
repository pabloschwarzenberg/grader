#Ordenar tres números
X = int(input("ingrese un numero:"))
Y = int(input("ingrese un segundo numero:"))
Z = int(input("ingrese un tercer numero:"))
ma = max(X,Y,Z)
mi = min(X,Y,Z)
D = (X + Y + Z) - ma - mi
print(mi ," , ", D ," , ",ma)