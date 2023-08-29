x1 = int(input("Ingrese el valor de el primer digito: "))
x2 = int(input("Ingrese el valor de el segundo digito: "))
x3 = int(input("Ingrese el valor de el tercer digito: "))

mayor = 0
medio = 0
menor = 0


if x1 > x2 and x1 >x3:
    mayor = x1 
    if x2 >= x3:
        medio, menor = x2, x3
    else:
        medio, menor = x3, x2
elif x2 >= x1 and x2 >= x3:
    mayor = x2
    if x1 >= x3:
        medio, menor = x1, x3
    else:
        medio, menor = x3, x1
else:
    mayor = x3
    if x3 >= x1:
        medio, menor = x1, x2
    else:
        medio, menor = x2, x1

print("El orden es",menor,",",medio,",",mayor)
