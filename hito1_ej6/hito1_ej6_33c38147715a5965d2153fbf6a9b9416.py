x=int(input("ingrese el primer valor:"))
y=int(input("ingrese el segundo valor:"))
z=int(input("ingrse el tercer valor:"))
a= min(x, y, z)
c= max(x, y, z)
b= (x+y+z)-a-c
print("Los numeros de menor a mayor son: {}, {}, {}".format(a,b,c))