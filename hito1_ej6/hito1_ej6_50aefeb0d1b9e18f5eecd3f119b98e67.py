x = int(input("ingrese el primer numero:"))
y = int(input("ingrese el segundo numero:"))
z = int(input("ingrese el tercer numero:"))

a = min(x, y, z)
c = max(x, y, z)
b = (x+y+z)-a -c

print("los numero ordenados son: {}, {} , {}".format(a,b,c))