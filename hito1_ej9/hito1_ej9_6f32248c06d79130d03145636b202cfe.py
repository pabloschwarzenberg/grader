#Sistema de Ecuaciones
numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))
numero_3 = int(input("Ingrese el numero 3: "))
numero_4 = int(input("Ingrese el numero 4: "))
numero_5 = int(input("Ingrese el numero 5: "))
numero_6 = int(input("Ingrese el numero 6: "))
a = numero_1*numero_5 - numero_2*numero_4
if a != 0:
    x = (numero_3*numero_5 - numero_2*numero_6) / a
    y = (numero_1*numero_6 - numero_3*numero_4) / a 
    print("x="+str(x))
    print("y="+str(y))