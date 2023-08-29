#Ordenar tres números
x = int(input("Ingrese el primer número:"))
y = int(input("Ingrese el segundo número:"))
z = int(input("Ingrese el tercer número:"))

if x>y>z:
    print("El orden de menor a mayor de los números ingresados es:", z,",", y,",", x)
if x>y<z:
    print("El orden de menor a mayor de los números ingresados es:", y, ",", z, ",", x)
if x<y<z:
    print("El orden de menor a mayor de los números ingresados es:", x, ",", y, ",", z)
if x<y>z:
    print("El orden de menor a mayor de los números ingresados es:", z, ",", x, ",",y )