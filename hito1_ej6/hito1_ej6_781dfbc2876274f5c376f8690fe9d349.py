#Ordenar tres números
print("Mira dame 3 numeros y los ordeno de menor a mayor")
x=int(input("Ingrese un numero:"))
y=int(input("Ingrese un segundo numero:"))
z=int(input("Ingrese un tercer numero:"))

if (x>y and y>z):
    print(z, ",", y, ",", x)
elif (x>z and z>y):
    print(y, ",", z, ",", x)
elif (y>x and x>z):
    print(z, ",", x, ",", y)
elif (y>z and z>x):
    print(x, ",", z, ",", y)
elif (z>x and x>y):
    print(y, ",", x, ",", z)
elif (z>y and y>x):
    print(x, ",", y, ",", z)
elif (x==y and y==z):
    print(x, ",", y, ",", z)
elif (x==y and y>z):
    print(z, ",", x, ",", y)
elif (x==y and y<z):
    print(y, ",", z, ",", x)
elif (x==z and z>y):
    print(y, ",", z, ",", x)
elif (x==z and z<y):
    print(z, ",", x, ",", y)
elif (z==y and y>x):
    print(x, ",", z, ",", y)
elif (z==y and y<x):
    print(z, ",", y, ",", x)
else:
    print("Valor Invalido")

        
    