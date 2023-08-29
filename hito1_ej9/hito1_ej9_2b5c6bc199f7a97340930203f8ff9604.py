#Sistema de Ecuaciones
n_1 = int(input("ingrese valor para N1: "))
n_2 = int(input("ingrese valor para N2: "))
n_3 = int(input("ingrese valor para N3: "))
n_4 = int(input("ingrese valor para N4: "))
n_5 = int(input("ingrese valor para N5: "))
n_6 = int(input("ingrese valor para N6: "))

m = n_1*n_5 - n_2*n_4

if m != 0:
    x =(n_3*n_5 - n_2*n_6) / m
    y =(n_1*n_6 - n_3*n_4) / m
    print("x=" +str(x) + "y=" +str(y))

else:
    print("no tiene solución")     