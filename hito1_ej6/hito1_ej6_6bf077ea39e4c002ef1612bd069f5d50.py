#Ordenar tres números
x = int(input(" Ingrese un numero :  "))
y = int(input(" Ingrese un segundo numero :  "))
z = int(input(" Ingrese un tercer numero :  "))
ma = max(x,y,z)
mi = min(x,y,z)
me = (x + y + z) - ma - mi
print(mi ,",", me, "," , ma)      