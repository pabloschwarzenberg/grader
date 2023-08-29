#Ordenar tres números
x= int(input("ingrese un numero"))
y=int(input("ingrese un segundo numero"))
z=int(input("ingrese un tercer nuemero"))
ma = max(x,y,z)
mi = min(x,y,z)
C = (x + y + z) - ma - mi
print(mi,",", C ,",",ma)