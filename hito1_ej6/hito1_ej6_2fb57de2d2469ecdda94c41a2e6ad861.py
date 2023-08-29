x=int(input("x: "))
y=int(input("y: "))
z=int(input("z: "))
if x>y>z:
    print(z,",",y,",",x)
if y>x>z:
    print(z,",",x,",",y)
if x>z>y:
    print(y,",",z,",",x)
if y>z>x:
    print(x,",",z,",",y)
if z>x>y:
    print(y,",",x,",",z)
if z>y>x:
    print(x,",",y,",",z)
if x==z==y:
    print(x,",",y,",",z)
if x==y>z:
    print(z,",",x,",",y)
if x==z>y:
    print(y,",",x,",",z)
if x==y<z:
    print(x,",",y,",",z)
if x==z<y:
    print(x,",",z,",",y)
if y==z>x:
    print(x,",",y,",",z)
if y==z<x:
    print(y,",",z,",",x)
