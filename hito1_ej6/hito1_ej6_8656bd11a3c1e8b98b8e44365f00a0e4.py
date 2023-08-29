#Ordenar números de Menor a mayor separados por coma

a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

#Inicializo las variables con el valor que ingresa el usuario, si son todos los valores iguales los mostrará tal como se envió
mayor = a
medio = b
menor = c


if a > b and a > c :
    mayor = a
    if b > c:
        medio = b
        menor = c
    else:
        medio = c
        menor = b
elif b > a and b > c :
    mayor = b
    if a > c:
        medio = a
        menor = c
    else:
        medio = c
        menor = a
elif c > b and c > b :
    mayor = c
    if a > b:
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print("Los números ordenados de menor a mayor son: " + str(menor)+ ", " + str(medio)+ ", " + str(mayor))
