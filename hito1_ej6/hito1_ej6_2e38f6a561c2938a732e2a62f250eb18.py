x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
z = int(input("Ingrese el tercer numero: "))

a = min(x,y,z)
b = max(x,y,z)
c = (x+y+z) - a - b

print("El nuevo orden de los numeros es {}, {}, {},".format(a,c,b))