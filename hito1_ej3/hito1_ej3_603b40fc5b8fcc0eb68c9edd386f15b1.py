#Aprobación de créditos
I = eval(input("Ingrese los ingresos en pesos chilenos, solo el numero: "))
A = eval(input("Ingrese el año de nacimiento: "))
N = eval(input("Ingrese la cantidad de hijos: "))
AP = eval(input("Ingrese la cantidad de años que pertenece al banco: "))
ES = input("Si es casado (C) o soltero (S): ")
V = input("Si vive en ciudad (U) o campo (R): ")
Edad = 2020 - A
if (AP > 10 and N >= 2):
    print("APROBADO")
else:
    if (ES == "C" and N > 3 and Edad >= 45 and Edad <= 55 ):
        print("APROBADO")
    else:
        if (I > 3500000 and AP > 5):
            print("APROBADO")
        else:
            if (I > 2500000 and ES == "S" and V == "U"):
                print("APROBADO")
            else:
                if( V == "R" and ES == "C" and N < 2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")      