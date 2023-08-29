#Ordenar tres números
print("ingrese 3 numeros enteros")
x = eval(input())
y = eval(input())
z = eval(input())
#x
if (x<=y<=z):
    print(x,",", y,",", z)
if (x<=z<=y):
    print(x,",", z,",", y)
#y
if (y<=x<=z):
    print( y,",", x,",", z)
if (y<=z<=x):
    print( y,",", z,",", x)
#z
if (z<=x<=y):
    print( z,",", x,",", y)
if (x<=y<=z):
    print( z,",", y,",", x)