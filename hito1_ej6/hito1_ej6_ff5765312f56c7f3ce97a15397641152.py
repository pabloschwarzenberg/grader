x=int(input("Ingrese el primer número: "))
y=int(input("Ingrese el segundo número: "))
z=int(input("Ingrese el tercer número: "))

a= min(x,y,z)
c= max(x,y,z)
b= (x + y + z) - a - c
print (a, ",", b, ",", c)