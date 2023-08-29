#Ordenar tres números
x= int(input("Ingrese un numero :"))
y= int(input("Ingrese un numero:"))
z= int(input("Ingrese un numero:"))
Max = max(x,y,z)
Min = min(x,y,z)
Medio = (x+y+z)-Max-Min
print("{0},{1},{2}".format(Min,Medio,Max))