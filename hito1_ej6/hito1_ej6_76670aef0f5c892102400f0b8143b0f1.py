#Ordenar tres números
x = eval(input("Ingrese el primer numero: "))
y = eval(input("Ingrese el segundo numero: "))
z = eval(input("Ingrese el tercero numero: "))
menor = 0
medio = 0
mayor = 0

if x < y and x < z:
    menor = x
    if y < z:
        medio = y
        mayor = z
    
    else:
        medio = z
        mayor = y

elif x < y and x > z:
    medio = x
    if y > z:
        mayor = y
        menor = z

elif x > y and x > z:
    mayor = x
    if y > z:
        medio = y
        menor = z

    else:
        medio = z
        menor = y

elif x > y and x < z:
    medio = x
    if y < z:
        menor = y
        mayor =z
elif x == y and x == z and z == y:
    menor = x
    medio = y
    mayor = z
elif x == y:
    if x < z:
        menor = x
        medio = y
        mayor = z
    else:
        menor = z
        medio = x
        mayor = y
elif x == z:
    if x < y:
        menor = x
        medio = z
        mayor = y
    else:
        menor = y
        medio =x
        mayor = z
else:
    if y == z:
        if y < x:
            menor = y
            medio = z
            mayor = x
        else:
            menor =x
            medio = y
            mayor = z

print(menor, ",",  medio,",",  mayor)