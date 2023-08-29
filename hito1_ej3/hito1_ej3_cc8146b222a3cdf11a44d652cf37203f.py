ingresos = int(input("Ingresos: "))
edad = int(input("Edad: "))
hijos = int(input("Cantidad de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil (S) o (C): ")
estado_civil = estado_civil.upper()
lugar = input("Vive en campo o ciudad (U) o (R): ")
lugar = lugar.upper()


if pertenencia > 10 and hijos >= 2:
    print("APROBADO")

elif estado_civil == "C" and hijos > 3 and 45 < edad < 55:
    print("APROBADO")

elif ingresos > 2500000 and estado_civil == "S" and lugar == "U":
    print("APROBADO")

elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")

elif lugar == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")