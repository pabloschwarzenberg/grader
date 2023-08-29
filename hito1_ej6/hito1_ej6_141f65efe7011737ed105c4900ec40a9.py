x=int(input("Ingrese primer número"))
y=int(input("Ingrese segundo número"))
z=int(input("Ingrese tercer número"))

if x<y and x<z:
    if y<z:
        print(x,end=",")
        print(y,end=",")
        print(z)
    if y==z:
        print(x,end=",")
        print(y,end=",")
        print(z)
    else:
        print(x,end=",")
        print(z,end=",")
        print(y)
if y<x and y<z:
    if x<z:
        print(y,end=",")
        print(x,end=",")
        print(z)
    if x==z:
        print(y,end=",")
        print(x,end=",")
        print(z)
    else:
        print(y,end=",")
        print(z,end=",")
        print(x)
if z<x and z<y:
    if x<y:
        print(z,end=",")
        print(x,end=",")
        print(y)
    if x==y:
        print(z,end=",")
        print(x,end=",")
        print(y)
    else:
        print(z,end=",")
        print(y,end=",")
        print(x)