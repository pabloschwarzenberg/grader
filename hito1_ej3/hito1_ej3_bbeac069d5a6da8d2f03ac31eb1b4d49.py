#Entrada
Ingresos = int(input("Ingrese la cantidad de sus ingresos[en pesos]= "))
Nacimiento = int(input("Ingrese su año de nacimiento= "))
Hijos = int(input("Numero de hijos= "))
Años = int(input("Hace cuantos años pertenese al banco= "))
Estado = input("Su estado civil[S:soltero/a, C:casado/a]: ")
Vive = input("Zona donde vive[U:urbano, R:rural]: ")

Edad = 2020 - Nacimiento


#Condiciones
if Años > 10 and Hijos >= 2:
    print("APROBADO")
elif Estado.upper() == "C" and Hijos > 3 and 45 <= Edad <= 55:
    print("APROBADO")
elif Ingresos > 2500000 and Estado.upper == "S" and Vive.upper == "U":
    print("APROBADO")
elif Ingresos > 3500000 and Años > 5:
    print("APROBADO")
elif Vive.upper() == "R" and Estado.upper() == "C" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      