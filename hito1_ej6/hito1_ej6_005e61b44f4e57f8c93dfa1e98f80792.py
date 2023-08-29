#Ordenar tres números
x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))
z = int(input('Ingrese el tercer número : '))
if x <= y <= z:
    menor = x
    medio = y
    mayor = z
if x <= z <= y:
    menor = x
    medio = z
    mayor = y
if y <= z <= x :
    menor = y
    medio = z
    mayor = x
if y <= x <= z :
    menor = y
    medio = x
    mayor = z
if z <= x <= y :
    menor = z
    medio = x 
    mayor = y
if z <= y <= x :
    menor = z
    medio = y 
    mayor = x
print('el orden es: ',menor, ',',medio,',',mayor)