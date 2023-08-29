#Ordenar tres números
x = int(input("Escriba el Primer Numero:"))
y = int(input("Escriba el Segundo Numero:"))
z = int(input("escriba el Tercer Numero:"))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print("los numeros ordenados son: {},{},{}".format(a,b,c))     