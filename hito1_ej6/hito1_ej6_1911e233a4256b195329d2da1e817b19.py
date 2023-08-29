#Ordenar tres números
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
c = int(input("Ingrese tercer numero: "))

if a < b:
    if a < c:
        if b < c:
            print("El orden de menor a mayor es: ", a, ",", b, ",", c)

        else:
            print("El orden de menor a mayor es: ", a, ",", c, ",", b)


if b < a:
    if b < c:
        if a < c:
            print("El orden de menor a mayor es: ", b, ",", a, ",", c)

        else:
            print("El orden de menor a mayor es: ", b, ",", c, ",", a)

if c < a:
    if c < b:
        if a < b:
            print("El orden de menor a mayor es: ", c, ",", a, ",", b)

        else:
            print("El orden de menor a mayor es: ", c, ",", b, ",", a)