#Ordenar tres números
x=eval(input('Ingresa el primer numero:'))
y=eval(input('Ingresa el segundo numero:'))
z=eval(input('Ingresa el tercer numero:'))
if x<y<z: 
    print('La posición de los números ordenados de menor a mayor es',x,',',y,',',z,)
if x<z<y:
    print('La posición de los números ordenados de menor a mayor es',x,',',z,',',y,)
if y<x<z:
    print('La posición de los números ordenados de menor a mayor es',y,',',x,',',z,)
if y<z<x:
    print('La posición de los números ordenados de menor a mayor es',y,',',z,',',x,)
if z<x<y:
    print('La posición de los números ordenados de menor a mayor es',z,',',x,',',y,)
if z<y<x:
    print('La posición de los números ordenados de menor a mayor es',z,',',y,',',x,)
if x==y<z:
    print('La posición de los números ordenados de menor a mayor es',x,',',y,',',z,)
if y==z<x:
    print('La posición de los números ordenados de menor a mayor es',y,',',z,',',x,)
if z==x<y:
    print('La posición de los números ordenados de menor a mayor es',z,',',x,',',y,)
if z==x==y:
    print('La posición de los números ordenados de menor a mayor es',z,',',y,',',x,)
