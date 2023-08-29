print('ingresa 3 numeros enteros y este programa te los ordenará de menor a mayor')
x=int(input('valor x:'))
y=int(input('valor y:'))
z=int(input('valor z:'))

if x<y<z:
    print('este es el orden de tus numeros:',x,',',y,',',z)
if x<z<y:
    print('este es el orden de tus numeros:',x,',',z,',',y)
if y<x<z:
    print('este es el orden de tus numeros:',y,',',x,',',z)
if y<z<x:
    print('este es el orden de tus numeros:',y,',',z,',',x)
if z<x<y:
    print('este es el orden de tus numeros:',z,',',x,',',y)
if z<y<x:
    print('este es el orden de tus numeros:',z,',',y,',',x)
if x==z==y:
    print('este es el orden de tus numeros:',x,',',z,',',y)
if x==z>y:
    print('este es el orden de tus numeros:',y,',',x,',',z)
if x==z<y:
    print('este es el orden de tus numeros:',z,',',x,',',y)
if y==z>x:
    print('este es el orden de tus numeros:',x,',',z,',',y)
if y==z<x:
    print('este es el orden de tus numeros:',y,',',z,',',x)
if y==x>z:
    print('este es el orden de tus numeros:',z,',',y,',',x)
if y==x<z:
    print('este es el orden de tus numeros:',x,',',y,',',z)