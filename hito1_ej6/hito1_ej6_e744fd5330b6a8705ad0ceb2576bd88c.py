x=eval(input('ingrese número: '))
y=eval(input('ingrese número: '))
z=eval(input('ingrese número: '))
if x<=y<=z:
    print(x,',',y,',',z)
if x<=y<z:
    print(x,',',y,',',z)
if x<y<=z:
    print(x,',',y,',',z)
if y<x<=z:
    print(y,',',x,',',z)
if z<=x<y:
    print(z,',',x,',',y)
if z<x<=y:
    print(z,',',x,',',y)
if z<=y<x:
    print(z,',',y,',',x)
