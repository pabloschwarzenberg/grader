x = int(input("Ingrese un primer número -> "))
y = int(input("Ingrese un segundo número -> "))
z = int(input("Ingrese un tercer número -> "))

if(x < y < z):
    print("xyz")
    print(x,",", y,",", z)

if(x < z < y):
    print("xzy")
    print(x,",", z,",", y)
    
if(y < x < z):
    print("yxz")
    print(y,",", x,",", z)

if(y < z < x):
    print("yzx")
    print(y,",", z,",", x)
    
if(z < y < x):
    print("zyx")
    print(z,",", y,",", x)
    
if(z < x < y):
    print("zxy")
    print(z,",", x,",", y)
    
if(x == y < z):
    print("x=yz")
    print(x,",", y,",", z)
    
if(x == z < y):
    print("x=zy")
    print(x,",", z,",", y)
    
if(y == z < x):
    print("y=zx")
    print(y,",", z,",", x) 
    
if(y == x < z):
    print("y=xz")
    print(y,",", x,",", z)
    
if(z == y < x):
    print("z=yx")
    print(z,",", y,",", x)
    
if(z == x < y):
    print("z=xy")
    print(z,",", x,",", y)
    
if(x < y == z):
    print("xy=z")
    print(x,",", y,",", z)
    
if(x < z == y):
    print("xz=y")
    print(x,",", z,",", y)
    
if(y < x == z):
    print("yx=z")
    print(y,",", x,",", z)
    
if(y < z == x):
    print("yz=x")
    print(y,",", z,",", x)
    
if(z < x == y):
    print("zx=y")
    print(z,",", x,",", y)
    
if(z < y == x):
    print("zy=x")
    print(z,",", y,",", x)