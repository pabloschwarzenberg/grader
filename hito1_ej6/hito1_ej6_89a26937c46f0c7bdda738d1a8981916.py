#Ordenar tres números
x = int(input('ingrese primer número '))
y = int(input('ingrese segundo número '))
z = int(input('ingrese tercer número '))
list = []
list.append(x)
list.append(y)
list.append(z)
list.sort()
mayor = x
if y > x and y > z:
    mayor = y
elif z > x and z > y:
    mayor = z
minor = x
if y < x and y < z:
    minor = y
elif z < x and z < y:
    minor = z   
medio = x
if x < y < z or x > y > z:
    medio = y
elif x < z < y or x > z > y:
    medio = z
print(list)