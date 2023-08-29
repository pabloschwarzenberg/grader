x=eval(input('ingrese el numero x:'))
y=eval(input('ingrese el numero y:'))
z=eval(input('ingrese el numero z:'))
if x<=y and x<=z and y<=z:
    print(x,',',y,',',z)
if y<=x and y<=z and x<=z:
    print(y,',',x,',',z)
if z<=x and z<=y and x<=y:
    print(z,',',x,',',y)
if x>=y and x>=z and y>=z:
    print(z,',',y,',',x)
