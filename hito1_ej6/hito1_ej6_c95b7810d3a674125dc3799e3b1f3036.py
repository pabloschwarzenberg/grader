#Ordenar tres números
# Entrada
x = int(input("Inserte un numero: "))
y = int(input("Inserte otro numero: "))
z = int(input("Inserte un ultimo numero: "))

# Procesamiento
a = min (x,y,z)
b = max (x,y,z)
c = (x+y+z) - a - b

# Salida
print("El orden es:  {}, {}, {}".format(a, c, b)) 