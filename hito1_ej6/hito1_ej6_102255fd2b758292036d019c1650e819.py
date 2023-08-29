v1 = int(input("ingrese un numero:"))
v2 = int(input("ingrese un segundo numero"))
v3 = int(input("ingrese un tercer numero"))
#orden
x = min(v1, v2, v3)
y = max(v1, v2, v3)
z = (v1 + v2 + v3) - x - y
#imprimir el orden
#print("el numero menor es:", x,"el numero del medio es:", y,"y el mayor es:",z)
print(x,",",z,",",y)