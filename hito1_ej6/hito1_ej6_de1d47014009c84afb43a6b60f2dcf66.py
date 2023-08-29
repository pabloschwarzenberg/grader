#Ordenar tres números
x = eval(input('ingrese un valor:'))
f = eval(input('ingrese un valor:'))
c = eval(input('ingrese un valor:'))
 
if x > f > c:
    print('El orden de menor a mayor es', c , ',' , f , ',' , x)
if x > c > f:
    print('El orden de menor a mayor es', f , ',' , c , ',' , x)
if f > x > c:
    print('El orden de menor a mayor es', c , ',' , x , ',' , f)
if f > c > x:
    print('El orden de menor a mayor es', x , ',' , c , ',' , f)
if c > f > x:
    print('El orden de menor a mayor es', x , ',' , f , ',' , c)
if c > x > f:
    print('El orden de menor a mayor es', f , ',' , x , ',' , c)
if x > f == c:
    print('El orden de menor a mayor es', x , ',' , c , ',' , f)
if f > c == x:
    print('El orden de menor a mayor es', c , ',' , f , ',' , x)
if c > f == x:
    print('El orden de menor a mayor es', f , ',' , c , ',' , x)
if f == c > x:
    print('El orden de menor a mayor es', x , ',' , c , ',' , f)
if c == x > f:
    print('El orden de menor a mayor es', f , ',' , c , ',' , x)
if f == x > c:
    print('El orden de menor a mayor es', c , ',' , x , ',' , f)
