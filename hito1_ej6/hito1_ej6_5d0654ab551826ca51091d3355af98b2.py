#Ordenar tres números
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))

if x<y<z:
    print(x,",",y,",",z)
elif x<z<y:
    print(x,",",z,",",y)
elif y<x<z:
    print(y,",",x,",",z)
elif y<z<x:
    print(y,",",z,",",x)
elif z<x<y:
    print(z,",",x,",",y)
elif z<y<x:
    print(z,",",y,",",x)
elif x==y==z:
    print(x,",",y,",",z)
elif x==y<z:
    print(x,",",y,",",z)
elif x==y>z:
    print(z,",",x,",",y)
elif x==z<y:
    print(x,",",z,",",y)
elif x==z>y:
    print(y,",",x,",",z)
elif y==z<x:
    print(y,",",z,",",x)
elif y==z>x:
    print(x,",",y,",",z)
      