#Ordenar tres números
x = int(input("Escribe el primer numero: "))
y = int(input("Escribe el segundo numero: "))
z = int(input("Escribe el tercer numero: "))

a = min(x,y,z)
b = (x + y + z) - a - c
c = max(x,y,z)
print("Los numeros ordenados son: {},{},{}".format(a,b,c)