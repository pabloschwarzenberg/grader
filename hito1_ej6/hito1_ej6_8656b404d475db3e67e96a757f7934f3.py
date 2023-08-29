#Ordenar tres números
x = int(input("Ingrese un numero:"))
y = int(input("ingrese un segundo número:"))
z = int(input("ingrese un tercer número:"))
ma = max(x,y,z)
mi = min(x,y,z)
D = (x+y+z) - ma - mi
print(mi,",",D,",",ma)