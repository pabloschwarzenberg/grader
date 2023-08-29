#Ordenar tres números
x = int(input("ingrese su numero:"))
y = int(input("ingrese un segundo numero:"))
z = int(input("ingrese un tercer numero:"))
ma = max(x,y,z)
mi = min(x,y,z)
D = (x + y + z) - ma - mi 
print(mi ," ," , D ,",",ma)