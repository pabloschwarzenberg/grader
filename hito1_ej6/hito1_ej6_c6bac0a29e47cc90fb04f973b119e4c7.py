#Ordenar tres números
x = int(input("Ingrese un número "))
y = int(input("Ingrese otro número "))
z = int(input("Ingrese otro número "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("los números ordenados son {}, {} , {}".format(a, b, c))