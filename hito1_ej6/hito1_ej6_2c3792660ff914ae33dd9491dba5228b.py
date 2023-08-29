x=int(input())
y=int(input())
z=int(input())

if x!=y and x!=z and y!=z:
    if x>y and x>z:
        if y>z:
            print(z,",",y,",",x)
        else:
            print(y,",",z,",",x)
    elif y>x and y>z:
        if x>z:
            print(z,",",x,",",y)
        else:
            print(x,",",z,",",y)
    else:
        if x>y:
            print(y,",",x,",",z)
        else:
            print(x,",",y,",",z)
elif x==y and x!=z:
    if x>z:
        print(z,",",x,",",y)
    else:
        print(x,",",y,",",z)
elif x==z and x!=y:
    if x>y:
        print(y,",",x,",",z)
    else:
        print(x,",",z,",",y)
else:
    print(x,",",y,",",z)