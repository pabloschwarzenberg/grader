#Ordenar tres números
x = int(input("ingrese un numero entero:"))
y = int(input("ingrese un numero entero:"))
z = int(input("ingrese un numero entero:"))

X = min(x,y,z)
Y = max(x,y,z)
Z = (x+y+z)-X-Y

print("los numeros ordenados son: {},{},{}".format(X,Z,Y))