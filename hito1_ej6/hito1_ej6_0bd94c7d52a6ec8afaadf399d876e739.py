#Ordenar tres números
#Entradas---------------
x = int(input("Ingrese el primer número entero: "))
y =int(input("Ingrese el segundo número entero: "))
z = int(input("Ingrese el tercer número entero: "))
    
#Proceso--------------------------------------------------------------

if x <= y and x <= z:
    if y <= z:
        print("El orden es:", x, ",", y, ",", z,".")
    elif z <= y:
        print("El orden es:", x, ",", z, ",", y,".")

elif y <= x and y <= z:
    if x <= z:
        print("El orden es:", y,",", x,",", z,".")
    elif z <= x:
        print("El orden es:", y,",", z,",", x,".")

elif z <= x and z <= y:
    if x <= y:
        print("El orden es:", z,",", x,",", y,".")
    elif y <= x:
        print("El orden es:", z,",", y,",", x,".")