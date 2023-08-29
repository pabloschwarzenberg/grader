X = eval(input("Ingrese un numero entero: "))
Y = eval(input("Ingrese otro numero entero: "))
Z = eval(input("Ingrese un tercer valor entero: "))
MAX = max (X,Y,Z)
MIN = min (X,Y,Z)
N = (X + Y + Z) - MIN - MAX
print (MIN," , ", N , " , ", MAX)